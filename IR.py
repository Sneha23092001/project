import RPi.GPIO as GPIO
#GPIO Python library (included with Raspbian) 
# lets you configure, read, and write to GPIO pins
import time

def checkIFFruitPresent():
  ir = 8
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(ir,GPIO.IN) 
  if GPIO.input(ir):
     time.sleep(1)
     return False
  else:
      time.sleep(1)
      return True
