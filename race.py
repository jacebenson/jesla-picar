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

speed = 0
mod = 5

while True:
    ch = getch()
    
#   if (abs(speed))+modifer < 100:
    if ch=='w':
        if speed+mod<=100:
            speed = speed + mod
    if ch=='s':
        if speed-mod>=-100:
            speed = speed - mod
    if ch=='a': #turn left
        explorerhat.motor.one.forwards(speed-10)
    if ch=='d': #turn right
        explorerhat.motor.two.forwards(speed-10)
    if speed>0 and speed<100:
        explorerhat.motor.forwards(speed)
    if speed>-100 and speed<0:
        explorerhat.motor.backwards(speed*-1)
    print(" " + str(speed))
    # else:
  #      print("At full speed")
#    explorerhat.pause()

