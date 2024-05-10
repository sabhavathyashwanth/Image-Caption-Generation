from flask import Flask, render_template, request
import pyttsx3
import numpy as np
from PIL import Image

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1


def predict_caption(image, max_length):
    # Placeholder function to generate a random caption
    caption = "This is a placeholder caption."
    return caption


def preprocess_image(image):
    # Placeholder function for image preprocessing
    # Resize image to 224x224, convert to numpy array, etc.
    processed_image = image.resize((224, 224))
    return processed_image


def generate_speech(text):
    # Placeholder function to generate speech from text
    # Use text-to-speech library like pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("/index.html")


@app.route("/after", methods=["POST", "GET"])
def after():
    file = request.files["img"]
    im = file.save("static/img.jpg")
    img = Image.open(file)
    processed_img = preprocess_image(img)
    caption = predict_caption(processed_img, 35)
    generate_speech(caption)
    return render_template("/predict.html", data=caption)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
