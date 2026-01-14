# 🌱 Krishi – সহায়ক
AI-Powered Smart Farming System

Growing with Nature using AI & IoT

# 📌 Project Overview

Krishi – সহায়ক is an AI + IoT–based smart farming system designed to assist farmers with data-driven decision-making.
The system provides smart irrigation, fertilizer optimization, crop recommendation, plant disease detection, and an AI chatbot for farming guidance.

The goal is to increase crop yield, reduce resource wastage, and make farming sustainable and intelligent.

# 🎯 Key Features

🌾 Crop Recommendation based on soil nutrients (NPK), pH, rainfall & temperature

💧 Smart Irrigation System using real-time soil moisture data

🧪 Fertilizer Optimization for improved soil health

🍃 Plant Disease Detection using Deep Learning (CNN)

🤖 AI Chatbot for farmer assistance (LLM-based)

📊 Web Dashboard for monitoring and analysis

🔌 IoT Integration using ESP32 & sensors

# 🧠 System Architecture

The system integrates:

IoT hardware for real-time data collection

AI/ML models for prediction and detection

Backend services for processing & decision logic

Web dashboard for user interaction

# 🗂️ Project Structure
Krishi-Sahayak/
│
├── Ai_bot_backend_agri/          # AI chatbot backend (LLM integration)
│
├── crop_recommendation_system/   # ML model for crop recommendation
│
├── Irrigation/                   # Smart irrigation logic & ESP32 integration
│
├── Irrigation Code/              # Microcontroller & sensor-level code
│
├── plant-disease-detection-system-main/
│   ├── model/                    # CNN model
│   ├── dataset/                  # Leaf disease dataset
│   └── inference/                # Disease prediction scripts
│
├── dashboard.html                # Farmer dashboard UI
├── dashboard.js                  # Dashboard logic
├── firebase.js                   # Firebase configuration
│
├── landing.html                  # Landing page
├── login.html                    # Login page
├── login.js                      # Authentication logic
│
├── styles.css                    # Common styles
├── log.css                       # Dashboard styles
│
├── assets/
│   ├── logo.png
│   ├── forest-agriculture.jpg
│   ├── img1.jpg
│   ├── img2.jpg
│   ├── img3.jpg
│   └── img4.jpg
│
└── README.md

# 🔁 Workflow Explanation
1️⃣ Smart Irrigation

Soil moisture sensor collects data

ESP32 sends data via Wi-Fi

Backend checks threshold

Relay activates water pump automatically

2️⃣ Crop & Fertilizer Recommendation

Input: NPK values, temperature, rainfall

ML model analyzes data

Outputs best crop and fertilizer suggestions

3️⃣ Disease Detection

Leaf image uploaded

CNN model detects disease

Outputs disease name and remedy

4️⃣ AI Chatbot

Farmers ask questions in simple language

LLM-based bot provides guidance

#🛠️ Technology Stack
Frontend

HTML, CSS, JavaScript

Backend

Python (Flask)

Machine Learning / Deep Learning

Scikit-learn

TensorFlow

Keras

Database & Cloud

Firebase


APIs

OpenWeatherMap API

Gemini API / LLMs

IoT Hardware

ESP32

Soil Moisture Sensor

Relay Module

Water Pump

# 🚀 End-Sem / Demo Capabilities

Web dashboard demo

Crop & fertilizer recommendation

Disease detection from image

Chatbot interaction

Automatic irrigation using ESP32

# 🔮 Future Enhancements

Fully responsive mobile-friendly web app

Multilingual chatbot with voice support

Crop yield prediction module

ML-based adaptive irrigation

Centralized database for historical analysis

# 👨‍💻 Team Members

Pratyush Basu

Soubhik Naskar

Trish Purkait

Arju Chakraborty


# 📜 License

This project is developed for academic and research purposes.
