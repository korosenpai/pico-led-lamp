from machine import Pin
import time

from neopixel import NeoPixel
strip = NeoPixel(Pin(0), 20)


# must create strip when relay is connected to led
# save state of led in some variable and recreate obj everytime
strip.fill((255, 255, 255))
strip.write()


time.sleep(5)
strip.fill((0, 0, 0))
strip.write()
del strip
