# Detect LED Morse Code
# Created by James Raphael Tiovalen (2020)

# Import libraries
import time
import cv2
import numpy as np
import imutils
import os
from collections import deque

# Load the BCM V4L2 driver for /dev/video0
os.system("sudo modprobe bcm2835-v4l2")
# Set the framerate
os.system("v4l2-ctl -p 30")

# Define morse code to character dictionary
morse2char = {
    "---.": "!",
    ".-..-.": "\"",
    "...-..-": "$",
    ".----.": "'",
    "-.--.": "(",
    "-.--.-": ")",
    ".-.-.": "+",
    "--..--": ",",
    "-....-": "-",
    ".-.-.-": ".",
    "-..-.": "/",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "---...": ":",
    "-.-.-.": ";",
    "-...-": "=",
    "..--..": "?",
    ".--.-.": "@",
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-.--.": "[",
    "-.--.-": "]",
    "..--.-": "_",
}

BEATMS = 200 / 1000

font = cv2.FONT_HERSHEY_DUPLEX

# Initialize camera and grab reference to raw video capture
cap = cv2.VideoCapture(0)

# Allow camera to warmup
time.sleep(2)

# Define green color range
lower_green = np.array([60, 170, 170])
upper_green = np.array([100, 255, 255])

# Define temporary variables to be used
msg = ""
chars = []
rxmsg = ""
final_string = []
flag = 0
pts = deque(maxlen=512)
ledoff = 0

# Main prediction logic
def calculate(frame):
	# Process video stream
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, lower_green, upper_green)
	masked_image = cv2.bitwise_and(frame, frame, mask = mask)
	h, s, v = cv2.split(masked_image)

	cnts, hierarchy = cv2.findContours(v, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	global msg
	global chars
	global rxmsg
	global final_string
	global flag
	global pts
	global ledoff

	# Check for existence of contours
	if cnts:
		flag += 1
		pts.appendleft(flag)
		ledoff = 0
	else:
		ledoff += 1
		flag = 0
		pts.appendleft(flag)

	for i in range(1, len(pts)):
		if pts[i] > pts[i-1]:
			if 11 <= pts[i] <= 12:
				print("Adding '-'")
				chars.append("-")
				pts = deque(maxlen=512)
				break

			elif 3 <= pts[i] <= 4:
				print("Adding '.'")
				chars.append(".")
				pts = deque(maxlen=512)
				break

	if 15 <= ledoff <= 16:
		msg = morse2char.get("".join(chars))

		if msg is not None:
			final_string.append(msg)
			rxmsg = "".join(final_string)

		if msg is None:
			chars = []

		chars = []

	if not cnts:
		cv2.putText(frame, "No morse code detected!", (10, 300), font, 1, (0, 0, 255), 3)
	elif rxmsg:
		cv2.putText(frame, "Deciphered message:\n" + rxmsg, (10, 300), font, 1, (0, 255, 0), 2)

	return frame

# Main loop
while(1):
	# Capture frames from camera
	ret, frame = cap.read()

	if ret == True:
		frame = calculate(frame)
		cv2.imshow("Frame Data", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# Clean up
cap.release()
cv2.destroyAllWindows()
cap.stop()