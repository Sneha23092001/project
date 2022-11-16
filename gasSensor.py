import RPi.GPIO as GPIO
import time
def checkIFFruitPresent():
  gasSensor = 22
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(gasSensor,GPIO.IN)
  if GPIO.input(gasSensor):
     time.sleep(1)
     #The sleep() function suspends(delays) execution 
     # of the current thread for the given number of seconds.
     return False
  else:
      time.sleep(1)
      return True
