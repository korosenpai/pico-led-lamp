""" DEFAULTS
color = (255, 191, 0)
brightness = 1
led_step = 1
"""

"""
import json
with open("config.json") as configfile:
    config = json.load(configfile)



import time
from led_strip import LED_STRIP
from machine import Pin, ADC

startup_button = Pin(1, Pin.IN, Pin.PULL_UP)
if not startup_button.value():
    # button is pressed
    pass
elif config["start_on_boot"]:
    print("starting..")
    import loop.py

"""
import test.led_optimizations.py



