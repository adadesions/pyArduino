import serial
import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

arduino = serial.Serial('/dev/ttyACM0', 9600)
cmd_dict = {
        'on': '1',
        'off': '0',
    }


def led_switch(led_id, cmd):
    cmd = str.lower(cmd)
    package = f'{led_id}{cmd_dict[cmd]}'
    print('(led_id, state) =', package)
    arduino.write(bytes(package, 'utf-8'))
    time.sleep(0.5)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/led/on/<led_id>')
def led_turn_on(led_id):
    led_switch(led_id, 'on')
    return render_template('index.html')


@app.route('/led/off/<led_id>')
def led_turn_off(led_id):
    led_switch(led_id, 'off')
    return render_template('index.html')