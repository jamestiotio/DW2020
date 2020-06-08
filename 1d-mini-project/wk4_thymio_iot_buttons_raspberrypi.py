import RPi.GPIO as GPIO
from libdw import pyrebase
from time import sleep

projectid = "thymio-iot"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = ""
email = ""
password = ""

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)

db = firebase.database()

# To create a new node with our own key
db.child("movement_list_ready").set(True, user['idToken'])

COMMAND_LIST = []
dankmode = True

GPIO.setmode(GPIO.BCM)

# For movement_now
CONTROLS_NOW = {12: "lft", 16: "fwd", 20: "rgt", 21: "stp"}

# For movement_list
CONTROLS_LIST = {12: "lft", 16: "fwd", 20: "rgt", 21: "go"}

if dankmode:
    for pin, direction in CONTROLS_NOW.items():
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
else:
    for pin, direction in CONTROLS_LIST.items():
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

while True:
    if dankmode:
        for pin in CONTROLS_NOW.keys():
            if GPIO.input(pin) == GPIO.HIGH:
                db.child("movement_now").set(CONTROLS_NOW.get(pin), user['idToken'])
                print(CONTROLS_NOW.get(pin), flush=True)  # Possibility for Netcat UDP
    else:
        '''
        We loop through the key (button name), value (gpio number) pair of the buttons
        dictionary and check whether the button at the corresponding GPIO is being
        pressed. When the OK button is pressed, we will exit the while loop and
        write the list of movements (movement_list) to the database. Any other button
        press would be stored in the movement_list.

        Since there may be debouncing issue due to the mechanical nature of the buttons,
        we can address it by putting a short delay between each iteration after a key
        press has been detected.
        '''
        
        for pin in CONTROLS_LIST.keys():
            if GPIO.input(21) == GPIO.HIGH:
                print("Sending command list...")
                db.child("movement_list").set(COMMAND_LIST, user['idToken'])
                db.child("movement_list_ready").set(True, user['idToken'])
                COMMAND_LIST = []
            elif GPIO.input(pin) == GPIO.HIGH:
                COMMAND_LIST.append(CONTROLS_LIST.get(pin))
                print(COMMAND_LIST)
                
        sleep(200/1000)
