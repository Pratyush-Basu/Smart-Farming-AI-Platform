from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
import google.generativeai as genai
import re
from dotenv import load_dotenv
app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure Gemini API
load_dotenv() 
genai.configure(api_key=os.getenv("api"))
model_gemini = genai.GenerativeModel('models/gemini-2.5-flash')

# Load model
model = tf.keras.models.load_model('best_model_resume.keras')

# Class names
class_names = [
    "bell pepper_bacterial spot",
    "bell pepper_healthy",
    "potato_early blight",
    "potato_late blight",
    "potato_healthy",
    "tomato_bacterial spot",
    "tomato_early blight",
    "tomato_late blight",
    "tomato_leaf mold",
    "tomato_septoria leaf spot",
    "tomato_spider mites",
    "tomato_target spot",
    "tomato_yellow leaf curl virus",
    "tomato_mosaic virus",
    "tomato_healthy"
]

IMG_SIZE = 256

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    class_index = np.argmax(preds)
    confidence = preds[0][class_index] * 100

    return class_names[class_index], round(confidence, 2)

def format_treatment_text(text):
    """Format markdown-style text to HTML"""
    # Replace **text** with <strong>text</strong>
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    
    # Replace * bullets with styled list items
    lines = text.split('\n')
    formatted_lines = []
    in_list = False
    
    for line in lines:
        line = line.strip()
        if line.startswith('* '):
            if not in_list:
                formatted_lines.append('<ul style="margin-left: 20px; margin-top: 10px;">')
                in_list = True
            formatted_lines.append(f'<li style="margin-bottom: 8px;">{line[2:]}</li>')
        else:
            if in_list:
                formatted_lines.append('</ul>')
                in_list = False
            if line:
                formatted_lines.append(f'<p style="margin-bottom: 10px;">{line}</p>')
    
    if in_list:
        formatted_lines.append('</ul>')
    
    return ''.join(formatted_lines)

def get_treatment_suggestion(plant_type, disease):
    """Get treatment suggestions using Gemini AI"""
    
    if "healthy" in disease.lower():
        return None, None
    
    # Short summary prompt
    summary_prompt = f"""You are an agricultural expert. A farmer detected {disease} in their {plant_type} plant.

Provide a SHORT summary (2-3 sentences max, under 50 words) of the most critical immediate action needed."""

    # Detailed prompt
    detail_prompt = f"""You are an agricultural expert. A farmer has detected {disease} in their {plant_type} plant.

Provide a detailed treatment recommendation with:
1. Immediate Actions (2-3 steps)
2. Chemical/Organic Treatment options
3. Preventive Measures (2-3 steps)

Keep it practical and actionable. Use bullet points."""

    try:
        # Get summary
        summary_response = model_gemini.generate_content(summary_prompt)
        summary = summary_response.text.strip()
        
        # Get full details
        detail_response = model_gemini.generate_content(detail_prompt)
        details = format_treatment_text(detail_response.text)
        
        return summary, details
    except Exception as e:
        print(f"Error: {e}")
        return "Unable to fetch treatment suggestions.", "Please consult a local agricultural expert."

@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        prediction=None,
        confidence=None,
        treatment_summary=None,
        treatment_details=None
    )

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    if file:
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save temporarily
        file.save(image_path)

        # Predict
        prediction, confidence = predict_image(image_path)

        # Delete image after prediction
        os.remove(image_path)

        # Get treatment suggestion if disease detected
        parts = prediction.split('_', 1)
        plant_type = parts[0] if len(parts) > 0 else "plant"
        disease = parts[1] if len(parts) > 1 else prediction
        
        treatment_summary, treatment_details = get_treatment_suggestion(plant_type, disease)

        return render_template(
            'index.html',
            prediction=prediction,
            confidence=confidence,
            treatment_summary=treatment_summary,
            treatment_details=treatment_details
        )
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)