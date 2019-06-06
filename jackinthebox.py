
#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import requests

import ast
from ast import literal_eval 

url = 'https://raw.githubusercontent.com/devopsbert/jackinthebox/master/switch.dat'
socket = literal_eval(requests.get(url).text)
print(socket)

GPIO.setmode(GPIO.BCM)

#init list with pin numbers
pinList = [2, 3, 4, 5]

#loop through pins and set mode and state to low
for i in pinList:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, GPIO.HIGH if socket[i-1] else GPIO.LOW)

#time to sleep between operations in the main loop
SleepTimeL = 0.2

try:
  while True:
    port = int(input("Enter plug number to switch: "))
    print(socket)
    socket[port] = not socket[port]
    print(socket)
    GPIO.output(port+1, GPIO.LOW if socket[port]  else GPIO.HIGH)


except KeyboardInterrupt:
  print("quit")
  GPIO.cleanup()