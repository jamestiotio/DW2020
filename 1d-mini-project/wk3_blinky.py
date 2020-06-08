import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED 1, GPIO24 for LED 2 and GPIO18 for switch
led = [23, 24]
switch = 18

# Set the GPIO23 and GPIO24 as output.
GPIO.setup(led, GPIO.OUT)

# Set the GPIO18 as input with a pull-down resistor.
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)

def blink(gpio_number, duration):
    '''This function takes in two input: gpio_number and duration. The
    gpio_number specifies the GPIO number which the LED (to be blinked) is
    connected to. The duration is the blink interval in seconds.'''

    GPIO.output(gpio_number, GPIO.HIGH)
    sleep(duration)
    GPIO.output(gpio_number, GPIO.LOW)
    sleep(duration)

GPIO.output(led[0],GPIO.LOW)
GPIO.output(led[1],GPIO.LOW)

while True:

        while GPIO.input(switch)==GPIO.LOW:
            GPIO.output(23, GPIO.LOW)
            blink(led[0],1)

        while GPIO.input(switch)==GPIO.HIGH:
            GPIO.output(24, GPIO.LOW)
            blink(led[1],1)