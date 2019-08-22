from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.rotation = 180  # rotate the image 0,90,180,270 degrees

camera.start_preview()
#camera.start_preview(alpha=200) # alpha level is 0 ~ 255
sleep(5)
camera.stop_preview()