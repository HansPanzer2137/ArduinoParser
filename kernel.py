import os
import sys
import time

import numpy
from Arduino import Arduino

red_light_pin= 11
green_light_pin = 10
blue_light_pin = 9


board = Arduino("115200", port="COM3") # plugged in via USB, serial com at rate 115200
board.pinMode(red_light_pin, "OUTPUT")
board.pinMode(green_light_pin, "OUTPUT")
board.pinMode(blue_light_pin, "OUTPUT")

def RGB_color(red_light_value, green_light_value, blue_light_value):
  board.analogWrite(red_light_pin, red_light_value)
  board.analogWrite(green_light_pin, green_light_value)
  board.analogWrite(blue_light_pin, blue_light_value)



while True:
    RGB_color(255, 0, 0)