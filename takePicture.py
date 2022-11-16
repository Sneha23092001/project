from picamera import PiCamera
from time import sleep
def click():
	with PiCamera() as camera:
		camera.start_preview()
		sleep(5)
		camera.capture('fruit_images/fruit.jpg')
		camera.stop_preview()
		print("Picture Captured")
