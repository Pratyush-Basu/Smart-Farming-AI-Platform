# 🌿 Krishi - সহায়ক: Plant Disease Detection System

An AI-powered web application for detecting plant diseases and providing treatment recommendations using Deep Learning and Google Gemini AI. This is a key module of the larger **Krishi Sohayak** project aimed at empowering farmers with intelligent agricultural solutions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-95.86%25-brightgreen.svg)

## 🎯 Features

- 🔍 **AI-Powered Disease Detection** - Deep learning CNN model with **95.86% accuracy**
- 🌾 **Multi-Crop Support** - Detects diseases in Bell Pepper, Potato, and Tomato plants
- 💊 **AI Treatment Recommendations** - Get instant, actionable treatment advice using Google Gemini 2.5 Flash
- 📊 **Confidence Scoring** - View prediction confidence levels with visual progress bars
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- 🎨 **Modern UI** - Clean, agricultural-themed interface with Bootstrap 5
- 🖼️ **Drag & Drop Upload** - Easy image upload with preview functionality
- 📖 **Expandable Details** - Concise summary with optional detailed treatment information

## 🌱 Supported Diseases

### Bell Pepper (2 classes)
- Bacterial Spot
- Healthy

### Potato (3 classes)
- Early Blight
- Late Blight
- Healthy

### Tomato (10 classes)
- Bacterial Spot
- Early Blight
- Late Blight
- Leaf Mold
- Septoria Leaf Spot
- Spider Mites (Two-spotted)
- Target Spot
- Yellow Leaf Curl Virus
- Mosaic Virus
- Healthy

**Total: 15 Disease Classes**

## 📊 Model Performance

- **Accuracy**: 95.86%
- **Training Dataset**: [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)
- **Total Images**: 20,600+ images
- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 256x256 pixels
- **Framework**: TensorFlow/Keras

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Deep Learning**: TensorFlow/Keras
- **AI Assistant**: Google Gemini API (2.5 Flash)
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Image Processing**: Pillow, NumPy

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key ([Get it here](https://aistudio.google.com/apikey))

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/trishpurkait/plant-disease-detection-system.git
cd plant-disease-detection-system
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up your Gemini API key**

Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_api_key_here
```

Or directly in `app.py`:
```python
genai.configure(api_key="your_api_key_here")
```

5. **Create required directories**
```bash
mkdir -p static/uploads
mkdir -p model
```

6. **Add your trained model**

Place your trained model file in the `model/` directory:
```
model/best_model_resume.keras
```

## 🏃 Running the Application

1. **Start the Flask server**
```bash
python app.py
```

2. **Open your browser**

Navigate to: `http://127.0.0.1:5000`

3. **Upload a plant image**
   - Click the upload area or drag & drop an image
   - Click "Analyze Plant" 🔍
   - View results with AI-powered treatment recommendations! 💊

## 📁 Project Structure

```
plant-disease-detection-system/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
│
├── model/
│   └── best_model_resume.keras # Trained TensorFlow model (95.86% accuracy)
│
├── static/
│   └── uploads/                # Temporary upload folder (auto-cleaned)
│
└── templates/
    └── index.html             # Main web interface
```

## 📦 Dependencies

```txt
Flask==3.0.0
tensorflow==2.15.0
numpy==1.24.3
Werkzeug==3.0.1
google-generativeai==0.3.2
Pillow==10.1.0
```

## 🔧 Configuration

### Model Configuration
Edit `app.py` to update model settings:
```python
IMG_SIZE = 256  # Image input size
class_names = [...]  # Update based on your model classes
```

### Gemini API Configuration
Adjust AI model settings:
```python
model_gemini = genai.GenerativeModel('models/gemini-2.5-flash')
```

Available models:
- `models/gemini-2.5-flash` - Fast and efficient (recommended)
- `models/gemini-2.5-pro` - More powerful, slower

## 🎓 How It Works

1. **Image Upload**: User uploads a plant leaf image (JPG, PNG, JPEG)
2. **Preprocessing**: Image is resized to 256x256 and normalized (scaled to 0-1)
3. **Disease Detection**: CNN model predicts disease class with confidence score
4. **AI Analysis**: If disease detected, Gemini AI generates:
   - Quick summary (2-5 critical actions)
   - Detailed treatment plan (expandable)
5. **Display Results**: 
   - Plant type and disease/status
   - Confidence percentage with visual bar
   - Formatted treatment recommendations with proper styling

## 🧪 Model Training Details

The CNN model was trained on the PlantVillage dataset with:
- **20,600+ images** across 15 classes
- **Image augmentation** for better generalization
- **Transfer learning** techniques
- **Final accuracy: 95.86%**

Dataset source: [PlantVillage on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)

Trained model of 1st part: [my_model_checkpoint.keras](https://drive.google.com/file/d/1MAXSIJ3yr55nIZB8Gs7KJB20y7P6uv4q/view?usp=drive_link)


Trained model of 2nd/final part: [best_model_resume.keras](https://drive.google.com/file/d/1cUWFmpSBmyXqG-iw_Mjl_LUGi3CwwL56/view?usp=drive_link)


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues & Limitations

- Images are deleted after prediction (no history maintained)
- Limited to 15 disease classes (3 crops)
- Requires stable internet connection for Gemini API calls
- Free Gemini API has rate limits (60 requests/minute)

## 🔮 Future Enhancements

- [ ] Add more crops and diseases (wheat, rice, corn)
- [ ] Implement prediction history and analytics
- [ ] Multi-language support (Hindi, Bengali, regional languages)
- [ ] Offline treatment database as fallback
- [ ] Mobile app version (Android/iOS)
- [ ] Integration with other Krishi Sohayak modules
- [ ] Real-time disease monitoring dashboard
- [ ] Community forum for farmers to share experiences

## 🌾 About Krishi Sohayak

This Plant Disease Detection System is part of **Krishi Sohayak** (Agricultural Assistant), a comprehensive platform designed to help farmers with:
- Crop disease detection and treatment
- Crop recommendation based on soil parameters
- Weather-based farming advice
- Market price predictions
- Expert consultation services

## 👥 Author

**Trish Purkait**
- GitHub: [@trishpurkait](https://github.com/trishpurkait)
- Email: trishpurkait@gmail.com

## 🙏 Acknowledgments

- [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease) for training data
- Google Gemini AI for intelligent treatment recommendations
- TensorFlow team for the deep learning framework
- Bootstrap team for the responsive UI framework
- Kaggle community for dataset hosting
- All farmers who inspire this work

## 📞 Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Email: trishpurkait@gmail.com
- Contributions and feedback are always welcome!

## ⭐ Show Your Support

If you find this project useful, please consider:
- Giving it a ⭐ star on GitHub
- Sharing it with others who might benefit
- Contributing to its development

---

<p align="center">Made with ❤️ for farmers and sustainable agriculture</p>
<p align="center">© 2025 Krishi - সহায়ক | Plant Disease Detection System</p>
<p align="center">Part of the Krishi Sohayak Project</p>
