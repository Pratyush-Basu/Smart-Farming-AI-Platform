import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("gemini_api"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_farmer_explanation(crop, area, soil, ideal, fertilizer, language="english"):

    fertilizer_text = ""
    if fertilizer:
        for name, qty in fertilizer.items():
            fertilizer_text += f"- {name}: {qty} kg\n"
    else:
        fertilizer_text = "No fertilizer required"

    prompt = f"""
You are an agriculture expert helping Indian farmers.

Explain the fertilizer recommendation in VERY SIMPLE language.
Avoid scientific or technical words.

Crop: {crop}
Land size: {area} acre

Soil nutrients:
Nitrogen: {soil['N']}
Phosphorus: {soil['P']}
Potassium: {soil['K']}

Ideal nutrients:
Nitrogen: {ideal['N']}
Phosphorus: {ideal['P']}
Potassium: {ideal['K']}

Recommended fertilizers:
{fertilizer_text}

Explain:
- What nutrient is low
- Which fertilizer to use
- How to apply
- When to apply
- After how many days apply again
- Advice for next 30–45 days
"""

    if language == "bengali":
        prompt += "\nExplain everything in very simple Bengali language."
    elif language == "hindi":
        prompt += "\nExplain everything in very simple Hindi language."
    else:
        prompt += "\nExplain everything in very simple English."

    response = model.generate_content(prompt)
    return response.text
