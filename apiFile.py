from auth import ReturnCredential

#Read credentials from file
rc = ReturnCredential('first-discovery-329912-adcfeb3480db.json')
rc.set_env_variable()

from fileRead import ReadFile

from flask import Flask, request
from flask import jsonify
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

import base64


from google.cloud import speech

speech_client = speech.SpeechClient()

import json



from setConfig import SetConfiguration

config_mp3 = 'config_mp3'
config_wav = 'config_wav'

sc = SetConfiguration(config_mp3,config_wav)
config_wav_config = sc.setWav()



def readFileWav(file):
        file_data = file.read()
        audio_wav = speech.RecognitionAudio(content=file_data)
        return audio_wav
    
    
@app.route('/voice', methods=['GET', 'POST'])
def add_message():
    print(request.is_json)
    content = request.get_json()
    wav_file = open("temp.wav", "wb")
    decode_string = base64.b64decode(content['file_string'])
    wav_file.write(decode_string)
    rf = ReadFile("temp.wav")
    audio_wav = rf.readFileWav()
    response_standard_mp3 = speech_client.recognize(
    config=config_wav_config,
    audio=audio_wav)
    transcribed_text = ''
    for result in response_standard_mp3.results:
        transcribed_text = transcribed_text + ' ' + result.alternatives[0].transcript
    
    
    return jsonify({"transcribed_text":transcribed_text})

if __name__ == '__main__':
    app.run()



