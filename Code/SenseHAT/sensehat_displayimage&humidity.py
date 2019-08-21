# reading and writing to the sensehat with python

# from sense_hat import SenseHat
from sense_emu import SenseHat
from time import sleep

mySenHa = SenseHat()

mySenHa.show_message("Hello", text_colour = [100,200,150])

mySenHa.load_image("raspberry.jpg")
sleep(5)

myHumidity = mySenHa.get_humidity()
humidString = str(myHumidity)
mySenHa.show_message(humidString)
