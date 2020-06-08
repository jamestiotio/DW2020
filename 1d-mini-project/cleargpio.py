# Reset all GPIO pins
# Created by Kenneth Chin Choon Hean (2020)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins = list(range(26))

GPIO.setup(pins, GPIO.OUT)

for i in pins:
	GPIO.output(i, 0)

