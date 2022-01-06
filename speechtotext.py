import os.path
import time
import os
from google.cloud import speech

def transcribe(bandymas):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'speech.json'
    client = speech.SpeechClient()
    try:
        with open(sound, 'rb') as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            enable_automatic_punctuation=True,
            sample_rate_hertz=44100,
            language_code='lt-LT',
            audio_channel_count=2,
        )

        response = client.recognize(config=config, audio=audio)
        for result in response.results:
            resultt = format(result.alternatives[0].transcript)
            return resultt

    except OSError:
        pass

sound = 'sound.wav'
transcribe(sound)