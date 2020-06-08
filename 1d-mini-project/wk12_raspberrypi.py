import RPi.GPIO as GPIO
from time import sleep
from libdw import pyrebase

projectid = "dw1d-gui"
url = "https://" + projectid + ".firebaseio.com"
apikey = ""

config={
    "apiKey":apikey,
    "databaseURL":url,
}

# Create a Firebase object by specifying the URL of the database and its secret token.
# The Firebase object has functions put and get, that allows user to put data onto
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Assign pin connection for LED.
leds = [23, 24]

# Set the pin layout to BCM layout
GPIO.setmode(GPIO.BCM)

# Set the pins corresponding to the LED as output.
GPIO.setup(leds, GPIO.OUT)

output = {'off': False, 'on': True}

while True:
    led_state = db.child('state').get().val() # Get the value from node named 'state'
    for i in range(2):
        GPIO.output(leds[i], output[led_state[i]['text']])

    sleep(0.5) # Read from database every 0.5 seconds