from machine import Pin
import time

from neopixel import NeoPixel
strip = NeoPixel(Pin(1), 20)

relay = Pin(0, Pin.OUT) # transistorts that enables relay

print("relay on")
relay.value(1) # relay on
time.sleep(0.2)


# must create strip when relay is connected to led
# save state of led in some variable and recreate obj everytime
strip.fill((255, 255, 255))
strip.write()


time.sleep(5)
relay.value(0)
del strip

print("relay off")
