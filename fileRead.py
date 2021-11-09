# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:22:23 2021

@author: user
"""

import os
from google.cloud import speech

class ReadFile():
    
    def __init__(self,file):
        self.file = file
        
    def readFileMp3(self):
        with open(self.file, 'rb') as f1:
            byte_data_mp3 = f1.read()
        audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)
        return audio_mp3
    
    def readFileWav(self):
        with open(self.file, 'rb') as f1:
            byte_data_wav = f1.read()
        audio_wav = speech.RecognitionAudio(content=byte_data_wav)
        return audio_wav