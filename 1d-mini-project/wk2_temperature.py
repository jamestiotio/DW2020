#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythymiodw import *

robot = ThymioReal()


def print_temp(t_celsius):
    """ Calculate t_fahrenheit and print both """

    t_fahrenheit = t_celsius * (9 / 5) + 32
    return (round(t_celsius, 3), round(t_fahrenheit, 3))


def forward(speed, duration):
    """ Move both wheels for that duration and then stop """

    robot.wheels(speed, speed)
    robot.sleep(duration)
    robot.wheels(0, 0)


speed = input("What is the speed (-100 to 100)? ")
duration = input("What is the duration (in seconds)? ")
forward(float(speed), float(duration))
temp = robot.temperature
print("The temperature in Celsius is", print_temp(temp)
      [0], "and Fahrenheit is", print_temp(temp)[1])
robot.quit()
