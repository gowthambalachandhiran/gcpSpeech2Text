# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:14:39 2021

@author: user
"""

import os
from google.cloud import speech
from google.oauth2 import service_account


class ReturnCredential():
    def __init__(self,file):
        self.file = file
        
    def set_env_variable(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.file
        speech_client = speech.SpeechClient()
        
        

