import json
import pickle
import os
import base64
import speech_recognition as sr
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pydub import AudioSegment
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'model', 'vectorizer.pkl')

# Load model safely
model = pickle.load(open(model_path, 'rb')) if os.path.exists(model_path) else None
vectorizer = pickle.load(open(vectorizer_path, 'rb')) if os.path.exists(vectorizer_path) else None


def home(request):
    return render(request, "index.html")


def speech_to_text(audio_base64):
    """Convert voice input to text"""
    recognizer = sr.Recognizer()

    # Decode base64 audio
    audio_data = base64.b64decode(audio_base64)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_data)
        temp_audio_path = temp_audio.name

    # Convert audio to text
    with sr.AudioFile(temp_audio_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
        except:
            text = ""

    return text


@csrf_exempt
def predict_spam(request):
    if request.method == "POST":
        data = json.loads(request.body)

        message = data.get("message", "")
        voice_data = data.get("voice", None)

        # If voice input exists
        if voice_data:
            message = speech_to_text(voice_data)

        if not message:
            return JsonResponse({"error": "No input provided"})

        if model and vectorizer:
            result = model.predict(vectorizer.transform([message]))[0]
            prediction = "Spam" if result == 1 else "Ham"
        else:
            prediction = "Model not found"

        return JsonResponse({
            "prediction": prediction,
            "text": message
        })

    return JsonResponse({"error": "Invalid request"})
