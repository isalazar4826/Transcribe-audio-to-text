
# Audio to Text Transcription App

This is a simple web application built with Flask that allows users to upload audio files and get the transcription using Google Cloud Speech-to-Text API. The app supports both `.mp3` and `.wav` files. Uploaded `.mp3` files are automatically converted to `.wav` format in mono before being sent for transcription.

## Features

- Upload audio files (`.mp3` or `.wav`).
- Converts `.mp3` files to `.wav` format (mono).
- Transcribes audio to text using Google Cloud Speech-to-Text API.
- Returns the transcribed text as a JSON response.

## Requirements

Before running the app, make sure you have the following installed:

- Python 3.6 or higher
- Flask
- pydub
- Google Cloud SDK
- Google Cloud Speech-to-Text API credentials

### Install Dependencies

You can install the necessary Python dependencies by running:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include the following libraries:

```
Flask==2.2.3
google-cloud-speech==3.10.0
pydub==0.25.1
```

## Google Cloud Setup

1. Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Google Cloud Speech-to-Text API** for your project.
3. Create a service account and download the **JSON credentials file**.
4. Set the environment variable for Google Cloud credentials in your system:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials-file.json"
```

For Windows users, use:

```bash
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\credentials-file.json
```

## Running the Application

To run the Flask app, execute the following command in your terminal:

```bash
python app.py
```

By default, the app will run locally on `http://127.0.0.1:5000/`.

### Uploading Audio

1. Open the web application in your browser.
2. Use the form to upload an audio file (either `.mp3` or `.wav`).
3. Once the file is uploaded, the app will process it and transcribe the audio to text.

The transcription will be displayed as a JSON response.

## Folder Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── upload_audio.html      # HTML file for uploading audio
└── speechkey.json          # Google Cloud API credentials (should be kept secret)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
