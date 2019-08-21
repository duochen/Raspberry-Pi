from sense_emu import SenseHat

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
print(humidity)