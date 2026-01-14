from flask import Flask, request, render_template
import numpy as np
import pickle
import json
import pandas as pd
from gemini_helper import generate_farmer_explanation


NPK_DF = pd.read_csv("ideal_npk.csv")
NPK_DF["crop"] = NPK_DF["crop"].str.lower()


app = Flask(__name__)

# =========================
# LOAD MODEL & ENCODER
# =========================
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("le.pkl", "rb") as f:
    le = pickle.load(f)

# =========================
# CONSTANTS
# =========================
ALL_CROPS = [
    "apple","banana","blackgram","chickpea","coconut","coffee",
    "cotton","grapes","jute","kidneybeans","lentil","maize",
    "mango","mothbeans","mungbean","muskmelon","orange",
    "papaya","pigeonpeas","pomegranate","rice","watermelon"
]

# =========================
# HOME
# =========================
@app.route("/")
def home():
    return render_template("index.html")

# =========================
# CROP RECOMMENDATION
# =========================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read inputs
        form_values = request.form.to_dict()
        input_values = {k: float(v) for k, v in form_values.items()}
        features = np.array(list(input_values.values())).reshape(1, -1)

        # Predict probabilities
        probs = model.predict_proba(features)[0]
        class_labels = le.inverse_transform(model.classes_)

        # Top 5 crops
        predictions = sorted(
            zip(class_labels, probs),
            key=lambda x: x[1],
            reverse=True
        )[:5]

        labels = [c for c, _ in predictions]
        values = [round(p * 100, 2) for _, p in predictions]
        top_crop = labels[0]

        return render_template(
            "index.html",
            top_crop=top_crop,
            labels=json.dumps(labels),
            values=json.dumps(values),
            prediction_text="Here are your top 5 recommended crops 🌾",
            inputs=input_values
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

# =========================
# FERTILIZER ENTRY (FROM CROP PAGE)
# =========================
@app.route("/fertilizer-entry", methods=["POST"])
def fertilizer_entry():

    top_crop = request.form.get("crop")  # MUST match hidden input name
    N = request.form.get("N")
    P = request.form.get("P")
    K = request.form.get("K")

    if not top_crop:
        return "❌ Crop not received"

    top_crop = top_crop.lower()

    return render_template(
        "fertilizer.html",
        source="crop",
        top_crop=top_crop,
        N=N, P=P, K=K,
        all_crops=ALL_CROPS
    )

# =========================
# DIRECT FERTILIZER PAGE
# =========================
@app.route("/fertilizer", methods=["GET"])
def fertilizer_direct():
    return render_template(
        "fertilizer.html",
        source="direct",        # 🔥 important flag
        all_crops=ALL_CROPS
    )

# =========================
# FERTILIZER RESULT
# =========================
from gemini_helper import generate_farmer_explanation

@app.route("/fertilizer-result", methods=["POST"])
def fertilizer_result():

    # -------- Get form inputs --------
    crop = request.form.get("crop")
    language = request.form.get("language", "english")  # ✅ NEW

    if not crop:
        return "Please select a crop"

    try:
        area = float(request.form.get("area"))
        soil = {
            "N": float(request.form.get("N")),
            "P": float(request.form.get("P")),
            "K": float(request.form.get("K"))
        }
    except:
        return "Invalid input values"

    crop = crop.lower()

    # -------- Fetch ideal NPK --------
    ideal_rows = NPK_DF[NPK_DF["crop"] == crop]
    if ideal_rows.empty:
        return f"No NPK data found for crop: {crop}"

    ideal_row = ideal_rows.iloc[0]
    ideal = {
        "N": ideal_row["N"],
        "P": ideal_row["P"],
        "K": ideal_row["K"]
    }

    # -------- Calculate deficiency --------
    deficiency = {
        "N": max(0, ideal["N"] - soil["N"]),
        "P": max(0, ideal["P"] - soil["P"]),
        "K": max(0, ideal["K"] - soil["K"])
    }

    # -------- Fertilizer calculation --------
    fertilizer = {}

    if deficiency["N"] > 0:
        fertilizer["Urea (46% N)"] = round((deficiency["N"] / 0.46) * area, 2)

    if deficiency["P"] > 0:
        fertilizer["DAP (46% P)"] = round((deficiency["P"] / 0.46) * area, 2)

    if deficiency["K"] > 0:
        fertilizer["MOP (60% K)"] = round((deficiency["K"] / 0.60) * area, 2)

    # -------- Gemini AI Explanation --------
    ai_explanation = generate_farmer_explanation(
        crop=crop,
        area=area,
        soil=soil,
        ideal=ideal,
        fertilizer=fertilizer,
        language=language  
    )

    ai_explanation = ai_explanation.replace("**", "")
    
    # -------- Render result page --------
    return render_template(
        "fertilizer_result.html",
        crop=crop,
        soil=soil,
        ideal=ideal,
        deficiency=deficiency,
        fertilizer=fertilizer,
        area=area,
        ai_explanation=ai_explanation,
        language=language  
    )
    



# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)
