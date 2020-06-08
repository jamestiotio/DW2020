from pythymiodw import *
from time import sleep
from libdw import pyrebase

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

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto
# the database and also retrieve data from the database.

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()

robot = ThymioReal()  # Create a robot object

running = True
dankmode = True
GottaGoFast = 500

# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)


def movebot(movement):
    if movement == 'fwd':
        robot.wheels(GottaGoFast, GottaGoFast)
    elif movement == 'lft':
        robot.wheels(-GottaGoFast, GottaGoFast)
    elif movement == 'rgt':
        robot.wheels(GottaGoFast, -GottaGoFast)
    elif movement == 'stp':
        robot.wheels(0, 0)


while running:
    if dankmode:
        movement_now = db.child("movement_now").get(user['idToken']).val()
        movebot(movement_now)
        # sleep(20/1000)

    else:
        # Check the value of movement_list in the database at an interval of 0.5
        # seconds. Continue checking as long as the movement_list is not in the
        # database (ie. it is None). If movement_list is a valid list, the program
        # exits the while loop and controls the robot to perform the movements
        # specified in the movement_list in sequential order. Each movement in the
        # list lasts exactly 1 second.

        print("Waiting for Ready!")
        movement_list_ready = db.child(
            "movement_list_ready").get(user['idToken']).val()
        if movement_list_ready:
            movement_list = db.child("movement_list").get(
                user['idToken']).val()
            print("READY!", movement_list)
            for movement in movement_list:
                movebot(movement)
                sleep(1)
            robot.wheels(0, 0)
            db.child("movement_list").set(["stp"], user['idToken'])
            db.child("movement_list_ready").set(False, user['idToken'])
        sleep(1)
