from machine import Pin
import time
from neopixel import NeoPixel
import json

with open("config.json") as configfile:
    config = json.load(configfile)

n = config["nleds"]
led_step = 2 # turn on every "led_step"th pixel
strip = NeoPixel(Pin(0), n)
strip.fill((0, 0, 0))

for i in range(n):
    if (i % led_step == 0):
        strip[i] = (int(255 * 0.1), int(191 * 0.1), 0)


strip.write()