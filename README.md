# Rotten Fruits and Vegetables Classifier

A Flask web application that classifies fruits and vegetables as healthy or rotten using deep learning.

## Features
- Image classification using pre-trained CNN model
- Web interface for easy use
- Supports multiple fruit/vegetable types
- Real-time predictions with confidence scores

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Rotten-Fruits-and-Vegetables-main.git
cd Rotten-Fruits-and-Vegetables-main
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

The model will automatically download from GitHub Releases on first run. This may take a few minutes depending on your internet connection.

Open your browser and go to: `http://localhost:5000`

## Model Download

The trained model is stored in GitHub Releases to keep the repository size small. When you run the application for the first time:
- `app.py` will automatically detect the missing model file
- It will download `healthy_vs_rotten.keras` from the GitHub Releases
- The model will be saved locally for future runs

If automatic download fails, you can manually download the model from:
**GitHub Releases** → Download `healthy_vs_rotten.keras` and place it in the project root directory.

## File Structure
```
├── app.py                          # Flask application
├── main.ipynb                      # Jupyter notebook with model training
├── class_names.json                # Class labels mapping
├── requirements.txt                # Python dependencies
├── templates/
│   ├── index.html                  # Home page
│   └── predict.html                # Prediction results page
├── static/
│   └── uploads/                    # User uploaded images (temporary)
└── healthy_vs_rotten.keras         # Model (auto-downloaded)
```

## Usage

1. Open the web application in your browser
2. Upload an image of a fruit or vegetable
3. Click "Predict"
4. The model will classify it as healthy or rotten with confidence score

## Technologies Used
- **Framework**: Flask
- **Deep Learning**: TensorFlow/Keras
- **Model**: VGG16 with fine-tuning
- **Frontend**: HTML/CSS

## Notes
- Model files are excluded from Git (see `.gitignore`)
- Model is downloaded from GitHub Releases automatically
- First run may take time to download the model

