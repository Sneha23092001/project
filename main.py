import IR as ir
import takePicture
import RPi.GPIO as GPIO
import tensorflowModel as tf
import time
led = 12
buzzer = 16
irSensor = 8
gasSensor = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(irSensor,GPIO.IN)
GPIO.setup(gasSensor,GPIO.IN)
while True:
	try:
		if(ir.checkIFFruitPresent()):
			print("Fruit Detected")
			try:
				takePicture.click()  #capture the Image
			except:
				print("Exiting Camera Module")
			print("Processing food Quality...")
			fruitQuality = tf.checkFruitQuality()
			if fruitQuality == "Rotten":
				print("Fruit Quality is: ", fruitQuality)
				GPIO.output(buzzer,True)
				GPIO.output(led,True)
				time.sleep(2)
			else:
				print("Fruit Quality is: ", fruitQuality)
				GPIO.output(buzzer,False)
				GPIO.output(led,False)
		else:
			print("Please put the Fruit")
			GPIO.output(buzzer,False)
			GPIO.output(led,False)
	except KeyboardInterrupt:
		GPIO.cleanup()
