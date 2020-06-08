from pythymiodw import *

robot = ThymioReal() # Create an object

robot.wheels(100, 100) # Make the robot move at same speed on both wheels
robot.sleep(5) # Wait for 5 seconds

robot.wheels(-50, 0) # Make the robot turn counter-clockwise with left moving
robot.sleep(2) # Wait for 2 seconds

robot.leds_top(0, 0, 32) # Turn on the top LED
robot.sleep(2) # Wait for 2 seconds
robot.leds_circle(led0=32) # Turn on the circle LED on the top
robot.sleep(2) # Wait for 2 seconds

robot.quit() # Disconnect the Bluetooth connection