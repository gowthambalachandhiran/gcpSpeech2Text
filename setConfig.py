# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:14:51 2021

@author: user
"""

import os
from google.cloud import speech

class SetConfiguration():
    
    def __init__(self,config_mp3,config_wav):
        self.config_mp3 = config_mp3
        self.config_wav = config_wav
        
    def setMp3(self):
        self.config_mp3 = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        enable_automatic_punctuation=True,
        language_code='en-US')
        return self.config_mp3
        
    def setWav(self):
        self.config_wav = speech.RecognitionConfig(
        enable_automatic_punctuation=True,
        sample_rate_hertz=48000,
        #language_code='en-US',
        language_code='en-IN',
        audio_channel_count=2)
        return self.config_wav
        
