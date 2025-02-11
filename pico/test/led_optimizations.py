from machine import Pin
import time
from neopixel import NeoPixel
import json

with open("config.json") as configfile:
    config = json.load(configfile)

n = config["nleds"]
led_step = 1 # turn on every "led_step"th pixel
brightness = 0.1
strip = NeoPixel(Pin(14), n)
strip.fill((0, 0, 0))

for i in range(n):
    if (i % led_step == 0):
        strip[i] = (int(255 * brightness), int(191 * brightness), 0)


strip.write()