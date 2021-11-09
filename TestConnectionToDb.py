# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:57:36 2021

@author: user
"""

import json

import psycopg2

with open('DBcredentials.json') as f:
  data = json.load(f)
  
def postgres_test():

    try:
        conn = psycopg2.connect(dbname=data["PGDATABASE"],user=data["PGUSER"],password=data["PGPASSWORD"],host=data["PGHOST"],port=data["PGPORT"])
        conn.close()
        return True
    
    except Exception as e: return e
    
print(postgres_test())