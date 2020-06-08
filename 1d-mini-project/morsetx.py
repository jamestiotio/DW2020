# Emit morse code using LED
# Created by Ragul Balaji (2020)

char2morse = {
  "!": "---.",
  "\"": ".-..-.",
  "$": "...-..-",
  "'": ".----.",
  "(": "-.--.",
  ")": "-.--.-",
  "+": ".-.-.",
  ",": "--..--",
  "-": "-....-",
  ".": ".-.-.-",
  "/": "-..-.",
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  ":": "---...",
  ";": "-.-.-.",
  "=": "-...-",
  "?": "..--..",
  "@": ".--.-.",
  "A": ".-",
  "B": "-...",
  "C": "-.-.",
  "D": "-..",
  "E": ".",
  "F": "..-.",
  "G": "--.",
  "H": "....",
  "I": "..",
  "J": ".---",
  "K": "-.-",
  "L": ".-..",
  "M": "--",
  "N": "-.",
  "O": "---",
  "P": ".--.",
  "Q": "--.-",
  "R": ".-.",
  "S": "...",
  "T": "-",
  "U": "..-",
  "V": "...-",
  "W": ".--",
  "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  "[": "-.--.",
  "]": "-.--.-",
  "_": "..--.-",
}

BEATMS = 200 / 1000

from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 23
GPIO.setup(led, GPIO.OUT)

print("MORSE CODE TX\nDW2019 19F07")

while True:
    GPIO.output(led, GPIO.LOW)
    txmsg = input("TX: ").upper()
    for word in txmsg.split(" "):
        for c in word:
            morsecode = char2morse[c]
            print(c, morsecode)
            for beat in morsecode:
                GPIO.output(led, GPIO.HIGH)
                if beat == '.': sleep(BEATMS * 1)
                elif beat == '-': sleep(BEATMS * 3)
                GPIO.output(led, GPIO.LOW)
                sleep(BEATMS * 1)
            sleep(BEATMS * 2)
        sleep(BEATMS * 4)
