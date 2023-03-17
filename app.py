# Flask imports
from flask import Flask, render_template
import datetime
import time

# Thirdpart imports
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO


app = Flask(__name__)

# Setup GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pins
red   = 13
green = 22

# Temperature
tempsensor = W1ThermSensor()

# Set pins as output
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

# Set pins to LOW
GPIO.output(green,False)
GPIO.output(red,False)
 

@app.route('/')
def index():
    return render_template('index.html')
            

@app.route('/get_temp')    
def get_current_temperature():
    temp = tempsensor.get_temperature()
    if round(temp) <= 23:
        print(temp)
        GPIO.output(green,False)
        GPIO.output(red,True)

    elif round(temp) >= 24:
        print(temp)
        GPIO.output(green,True)
        GPIO.output(red,False)
        
    return str(round(temp,2))+'&#8451'

@app.route('/get_current_datetime')     
def get_current_datetime():
    return (datetime.datetime.now()).strftime('%H:%M')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
