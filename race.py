#!/usr/bin/env python

print("Press CTRL+C to exit.")

import sys, tty, termios, time, explorerhat

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

speed = 60
mod = 5
speed1 = 60
speed2 = 60
# at 60 both motors work.. make 60 my base number.
while True:
    ch = getch()
    if ch=='w':
        speedN = max(speed1, speed2, 60)
        speed1 = speedN + mod
        speed2 = speedN + mod
    if ch=='s':
        speedN = min(speed1, speed2, -60)
        speed1 = speedN - mod
        speed2 = speedN - mod
    if ch=='a': #turn left
        speed1 = 100
        speed2 = 0
    if ch=='d': #turn right
        speed1 = 0
        speed2 = 100
    if speed1>100:
        speed1 = 100
    if speed1<-100:
        speed1 = -100
    if speed2>100:
        speed2 = 100
    if speed2<-100:
        speed2 = -100
    print(" speed1: " + str(speed1) + " speed2: " + str(speed2))
    explorerhat.motor.one.speed(speed1)
    explorerhat.motor.two.speed(speed2)

    #print(" speed: " + str(speed) + " speed1: " + str(speed1) + " speed2: " + str(speed2))
    
    if ch=='1':
        speed1 = speed1 + mod
        explorerhat.motor.one.speed(speed1)
    if ch=='2':
        speed2 = speed2 + mod
        explorerhat.motor.two.speed(speed2)
