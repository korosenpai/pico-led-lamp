from machine import Pin, ADC
import time

btn1 = Pin(13, Pin.IN, Pin.PULL_UP)
if not btn1.value():
    print("Button1 is Pressed")
else:
    print("Button1 is not Pressed")
    
   
   
potentiometer = ADC(Pin(28))

while True: # Loop forever

    print(potentiometer.read_u16()) # Read the potentiometer value

    time.sleep(0.5) # Wait a second
