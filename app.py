import os
from flask import Flask, request, jsonify, render_template
from google.cloud import speech
from pydub import AudioSegment
import io

app = Flask(__name__)

# Configura la variable de entorno para las credenciales de Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\\Users\\isala\\Downloads\\Transcribe-audio-to-text\\speechkey.json'

# Ruta para servir el archivo HTML
@app.route('/')
def index():
    return render_template('upload_audio.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    # Verifica si se envió un archivo en la solicitud
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    audio_file = request.files['file']

    # Verifica si el archivo es .mp3 y conviértelo a .wav en mono si es necesario
    if audio_file.filename.endswith('.mp3'):
        # Carga el archivo .mp3 en pydub
        audio = AudioSegment.from_file(io.BytesIO(audio_file.read()), format="mp3")
        # Convierte a mono y luego a formato wav
        audio = audio.set_channels(1)
        audio_content = io.BytesIO()
        audio.export(audio_content, format="wav")
        audio_content = audio_content.getvalue()
        # Obtén la frecuencia de muestreo del archivo convertido
        sample_rate = audio.frame_rate
    else:
        # Si no es mp3, asume que ya es un wav compatible
        audio = AudioSegment.from_file(io.BytesIO(audio_file.read()), format="wav")
        # Convierte a mono si es necesario
        if audio.channels > 1:
            audio = audio.set_channels(1)
        audio_content = io.BytesIO()
        audio.export(audio_content, format="wav")
        audio_content = audio_content.getvalue()
        sample_rate = audio.frame_rate

    try:
        # Configura el cliente de Google Cloud Speech-to-Text
        client = speech.SpeechClient()

        # Crea un objeto RecognitionAudio con el contenido del archivo
        audio = speech.RecognitionAudio(content=audio_content)

        # Configuración para la transcripción con la frecuencia de muestreo detectada
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate,
            language_code="es-ES"
        )

        # Realiza la solicitud de transcripción a la API
        response = client.recognize(config=config, audio=audio)

        # Procesa el resultado de la transcripción
        result_text = ""
        for result in response.results:
            result_text += result.alternatives[0].transcript + " "

        # Devuelve la transcripción como respuesta
        return jsonify({"transcription": result_text})

    except Exception as e:
        # Maneja errores de transcripción y retorna un mensaje adecuado
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
