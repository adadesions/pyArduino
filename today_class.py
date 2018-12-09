import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)

cmd_dict = {
    'on': '1',
    'off': '0'
}
led_id = input('Which LED?[0-2]: ')
cmd = input('Turn on/Turn off[on/off]: ')
cmd = str.lower(cmd)
state = led_id+cmd_dict.get(cmd, 'off')
# state = f'{led_id}{cmd_dict.get(cmd, 'off')}'
time.sleep(2)
arduino.write(bytes(state, 'utf-8'))
