
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#init list with pin numbers
pinList = [2, 3, 4, 5]

#loop through pins and set mode and state to low
for i in pinList:
  GPIO.setup(i, GPIO.OUT)
  GPIO.output(i, GPIO.HIGH)

#time to sleep between operations in the main loop
SleepTimeL = 0.2
socket = {
    1: False,
    2: False,
    3: False,
    4: False
}

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