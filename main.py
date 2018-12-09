import serial
import time
import random

import click


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


@click.group()
def main():
    '''
    CLI Toolkits for simple control LED and other things with Arduino.\n
    Author: Ada92k\n
    Version: 0.5.0
    '''
    pass


@main.command('control-led', short_help='To turn LED light on/off')
@click.option('--led_id', prompt='Enter LED Id', default=0, help='Index number of LED light[0-9]' )
@click.option('--turn', prompt='Selete LED state[on/off]', default='on', help='[on/off]' )
def control_led(led_id, turn):
    print(f'LED{led_id} state is', turn)
    led_switch(led_id, turn)


@main.command('all-on', short_help='Turn on all LED light')
@click.option('--num_led', prompt='Number of LED light', default=1, help='Number of LED to turn on')
def turn_on_all(num_led):
    states = [ (index, 'on') for index in range(num_led)]
    for state in states:
        led_switch(state[0], state[1])
        time.sleep(2)


@main.command('random_blink', short_help='Do random blink with LED light')
@click.option('--delay', prompt='Number of time delay', default=1.0, help='Delay time to do blink')
def do_rand_blink(delay):
    states = ['on', 'off']
    while True:
        count = random.randint(0, 5)
        led_id = count%3
        cmd = states[count%2]
        led_switch(led_id, cmd)
        time.sleep(delay)


@main.command('blink', short_help='Do blink with LED light')
@click.option('--num_led', prompt='Number of LED light', default=1, help='Number of LED')
@click.option('--delay', prompt='Number of time delay', default=1.0, help='Delay time to do blink')
def do_blink(num_led, delay):
    states = ['off', 'on']
    leds = [[idx, 1] for idx in range(num_led)]
    while True:
        for i, led in enumerate(leds):
            led_switch(led[0], states[led[1]])
            leds[i][1] = (led[1]+1)%2
            time.sleep(delay)



if __name__ == '__main__':
    main()