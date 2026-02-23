
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
import urllib.request
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# GitHub model download configuration
MODEL_URL = "https://github.com/YOUR_USERNAME/Rotten-Fruits-and-Vegetables-main/releases/download/v1.0/healthy_vs_rotten.keras"
MODEL_FILE = 'healthy_vs_rotten.keras'

def download_model():
    """Download model from GitHub Releases if not present"""
    if not os.path.exists(MODEL_FILE):
        print(f"Downloading model from {MODEL_URL}...")
        try:
            urllib.request.urlretrieve(MODEL_URL, MODEL_FILE)
            print(f"Model downloaded successfully to {MODEL_FILE}")
        except Exception as e:
            print(f"Error downloading model: {e}")
            raise Exception(f"Failed to download model. Please download manually from GitHub Releases.")

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Download model if needed
download_model()

with open("class_names.json", "r") as f:
    class_names = json.load(f)

class_names = {int(k): v for k, v in class_names.items()}
model = load_model(MODEL_FILE)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Image preprocessing
            img = load_img(filepath, target_size=(224, 224))
            x = img_to_array(img)
            x = preprocess_input(x)
            x = np.expand_dims(x, axis=0)

            preds = model.predict(x)
            class_id = np.argmax(preds)
            label = class_names[class_id]
            confidence = float(np.max(preds)) * 100
            # label = class_names.get(class_id, "Unknown")

            return render_template(
                'predict.html',
                prediction=label,
                confidence=round(confidence, 2),
                image_path=filepath
            )

    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
