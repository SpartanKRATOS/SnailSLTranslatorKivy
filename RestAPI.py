from flask import Flask, jsonify, request
from time import sleep
from serial import Serial
from flask_cors import CORS, cross_origin
import subprocess
import cv2
import numpy as np
import os
import signal
import subprocess


from matplotlib import pyplot as plt
import time
import mediapipe as mp
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard


import sys



# Rest API
app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content_Type'
@app.route('/action', methods = ['POST','GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def get_data():
    if request.method == 'POST':
        rq = request.get_json()
        order = rq['order']
        print(order)
        if order == "run":
            try:
                    #recognition = open(r'/home/pi/Desktop/SNAILTranslation/SnailSLTranslatorKivy-main/actionDetection.py','r').read()
                    
                    #exec(recognition)
                p = subprocess.Popen(['python3', '/home/pi/Desktop/SNAILTranslation/SnailSLTranslatorKivy-main/actionDetection.py'])
                
                sleep(200)
                p.kill()
                return jsonify(order)
            except (IndexError, IOError) as e:
             
                return jsonify({'error': e.message}), 503
            
        
    if request.method == 'GET':
        try:
            
            WORDS = ""
            with open("/home/pi/Desktop/SNAILTranslation/SnailSLTranslatorKivy-main/translation.txt", "r") as file:
                WORDS = file.read()
            return jsonify(WORDS)

        except (IndexError, IOError) as e:
     
            return jsonify({'error': e.message}), 503
        
@app.route('/action/stop', methods = ['GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def stop():
   
    pid = get_pid()
    os.kill(pid, signal.SIGTERM)
    return 'done'
                  
  
def get_pid():
    return int(subprocess.check_output(['pgrep', '-f', '/home/pi/Desktop/SNAILTranslation/SnailSLTranslatorKivy-main/actionDetection.py']).strip())
try:
    app.run()

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Closing serial port and exiting...")

