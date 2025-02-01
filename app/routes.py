from flask import Flask, render_template, request
from services.tts_service import synthesize_text
from services.stt_service import transcribe_audio
from services.pdf_service import extract_text_from_pdf, summarize_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.form['text']
    language = request.form['language']
    gender = request.form['gender']
    synthesize_text(text, language, gender)
    return "Text to Speech completed!"

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    audio_file = request.files['audio']
    audio_file_path = "audio.wav"
    audio_file.save(audio_file_path)
    transcript = transcribe_audio(audio_file_path)
    return transcript

@app.route('/pdf-to-speech', methods=['POST'])
def pdf_to_speech():
    pdf_file = request.files['pdf']
    pdf_file_path = "file.pdf"
    pdf_file.save(pdf_file_path)
    text = extract_text_from_pdf(pdf_file_path)
    synthesize_text(text)
    return "PDF to Speech completed!"

@app.route('/pdf-summary', methods=['POST'])
def pdf_summary():
    pdf_file = request.files['pdf']
    pdf_file_path = "file.pdf"
    pdf_file.save(pdf_file_path)
    text = extract_text_from_pdf(pdf_file_path)
    summary = summarize_text(text)
    return summary
