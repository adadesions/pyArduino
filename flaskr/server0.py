from flask import Flask
from flask import render_template

import serial
import time

app = Flask(__name__)
arduino = serial.Serial('/dev/ttyACM0', 9600)

cmd_dict = {
    'on': '1',
    'off': '0'
}

@app.route('/')
def index():
    return render_template('home.html')
    # return render_template('index.html')


@app.route('/led/on/<led_id>')
def turn_on(led_id):
    state = led_id+'1'
    time.sleep(2)
    arduino.write(bytes(state, 'utf-8'))

    return render_template('home.html')


@app.route('/led/off/<led_id>')
def turn_off(led_id):
    state = led_id+'0'
    time.sleep(2)
    arduino.write(bytes(state, 'utf-8'))

    return render_template('home.html')

if __name__ == '__main__':
    app.run()
