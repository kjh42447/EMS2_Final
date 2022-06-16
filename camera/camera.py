from picamera import PiCamera
from time import sleep

camera = PiCamera()

#camera.rotation = 180
camera.start_preview()    #alpha=(0~255)
sleep(5)
camera.capture('image001.jpg')
camera.stop_preview()