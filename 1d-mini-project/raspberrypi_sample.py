import RPi.GPIO as GPIO

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED and GPIO18 for switch
led = 23
switch = 18

# Set GPIO23 as output.
GPIO.setup(led, GPIO.OUT)

# Set GPIO18 as input with a pull-down resistor.
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)

while True:
    if GPIO.input(switch) == GPIO.HIGH:  # Switch is connected
        GPIO.output(led, GPIO.HIGH)  # Turn on the LED
    else:  # Switch is disconnected
        GPIO.output(led, GPIO.LOW)  # Turn off the LED