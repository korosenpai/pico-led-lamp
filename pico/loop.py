import time
from led_strip import LED_STRIP
from machine import Pin, ADC

strip = LED_STRIP(0, 20)
strip.set_color(255, 191, 0)

btn = Pin(1, Pin.IN, Pin.PULL_UP)

   
potentiometer = ADC(Pin(28))


while True:
    
    brightness = potentiometer.read_u16() / 65535
    brightness = max(round(brightness, 1), 0.1)
    #print("brightness:", brightness)
    
    strip.set_brightness(brightness)
    
    strip.update()
    time.sleep(1)


strip.set_off().update()
del strip
