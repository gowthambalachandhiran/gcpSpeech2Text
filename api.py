# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:35:57 2021

@author: user
"""

from auth import ReturnCredential

#Read credentials from file
rc = ReturnCredential('first-discovery-329912-adcfeb3480db.json')
rc.set_env_variable()

#Creating empty dataframe and writing 
#empty_book = pd.DataFrame(columns = ['patient_id','date','q3_a','q3_b','q3_c'])
#writer = pd.ExcelWriter('demo.xlsx', engine='openpyxl')




import pandas as pd
from openpyxl import load_workbook
from flask import Flask, request
from flask import jsonify
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

import os
from google.cloud import speech

speech_client = speech.SpeechClient()

import json

import ast

from setConfig import SetConfiguration

config_mp3 = 'config_mp3'
config_wav = 'config_wav'

sc = SetConfiguration(config_mp3,config_wav)
config_wav_config = sc.setWav()

def readFileWav(file):
        file_data = file.read()
        audio_wav = speech.RecognitionAudio(content=file_data)
        return audio_wav


@app.route('/transcribe', methods=['GET', 'POST'])
def add_message():
    content = request.files['file']
    res = request.form.getlist('Patient-Details')
    form_data = ast.literal_eval(res[0])
    patient_id = form_data['Patient-Id']
    date_of_service = form_data['DOS']
    #patiend_id = res[0]['Patient-Id']
    #date_of_serivce = res[0]['DOS']
    wav_file =  readFileWav(content)
    ## Step 3. Transcribing the RecognitionAudio objects
    response_standard_mp3 = speech_client.recognize(
    config=config_wav_config,
    audio=wav_file
)
    transcribed_text = ''
    for result in response_standard_mp3.results:
        transcribed_text = transcribed_text + ' ' + result.alternatives[0].transcript
        
    if "hbaic" in  transcribed_text.lower():
        q_1 = "HBAIC done"
    else:
        q_1 = None
    
    if "bp" in transcribed_text.lower() or "blood pressure" in transcribed_text.lower():
        q_2 = "Blood pressure test done"
    else:
        q_2 = None
        
    if "ldl" in transcribed_text.lower():
        q_3 = "LDL test done"
    else:
        q_3 = None
        
    if "hdl" in transcribed_text.lower():
        q_4 = "HDL test done"
    else:
        q_4 = None
        
    if "ecg" in transcribed_text.lower():
        q_5 = "ecg test done"
    else:
        q_5 = None
        
    if q_1 == None and q_2 == None and q_3 == None and q_4 == None and q_5 == None:
        q_6 = "Please specify again"
    else:
        q_6 = None
        
    return jsonify({"text":transcribed_text,"PID":patient_id,"DOS":date_of_service,"q1":q_1,"q2":q_2,"q3":q_3,"q4":q_4,"q5":q_5,"q6":q_6})


if __name__ == '__main__':
    app.run(host= '127.0.0.1',debug=True,use_reloader=False)