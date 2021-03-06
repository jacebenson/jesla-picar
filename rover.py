#!/usr/bin/env python3

from gpiozero import PWMOutputDevice
from time import sleep
import sys, tty, termios

#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 13	# IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive

# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

def allStop():
  print('allStop')
  forwardLeft.value = 0
  reverseLeft.value = 0
  forwardRight.value = 0
  reverseRight.value = 0

def forwardDrive():
  print('forwardDrive')
  forwardLeft.value = 1.0
  reverseLeft.value = 0
  forwardRight.value = 1.0
  reverseRight.value = 0

def reverseDrive():
  print('reverseDrive')
  forwardLeft.value = 0
  reverseLeft.value = 1.0
  forwardRight.value = 0
  reverseRight.value = 1.0

def spinLeft():
  print('spinLeft')
  forwardLeft.value = 0
  reverseLeft.value = 1.0
  forwardRight.value = 1.0
  reverseRight.value = 0

def SpinRight():
  print('spinRight')
  forwardLeft.value = 1.0
  reverseLeft.value = 0
  forwardRight.value = 0
  reverseRight.value = 1.0

def forwardTurnLeft():
  print('forwardTurnLeft')
  forwardLeft.value = 0.2
  reverseLeft.value = 0
  forwardRight.value = 0.8
  reverseRight.value = 0

def forwardTurnRight():
  print('forwardTurnRight')
  forwardLeft.value = 0.8
  reverseLeft.value = 0
  forwardRight.value = 0.2
  reverseRight.value = 0

def reverseTurnLeft():
  print('reverseTurnLeft')
  forwardLeft.value = 0
  reverseLeft.value = 0.2
  forwardRight.value = 0
  reverseRight.value = 0.8

def reverseTurnRight():
  print('reverseTurnRight')
  forwardLeft.value = 0
  reverseLeft.value = 0.8
  forwardRight.value = 0
  reverseRight.value = 0.2

print("Press CTRL+C to exit.")

def getch():
  import sys, tty, termios
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch

while True:
  ch = getch()
  if ch=='w' or ch=='8':
    forwardDrive()
  if ch=='s' or ch=='2':
    reverseDrive()
  if ch=='a' or ch=='4': #turn left
    spinLeft()
  if ch=='d' or ch=='6': #turn right
    SpinRight()
  if ch=='5':
    allStop()
