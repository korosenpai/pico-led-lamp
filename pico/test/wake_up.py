
import machine
import time

# Configure the button pin
button_pin = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Set up an interrupt to wake from sleep
def wake_callback(pin):
    print("Waking up from light sleep!")
    import test.relay_test

button_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=wake_callback)

# Simulate some activity before sleep
print("Going into light sleep. Press the button to wake up.")
machine.deepsleep()  # The Pico will sleep and wake on interrupt

# Resume execution after waking up
print("Pico woke up!")
led = Pin(25, Pin.OUT)

led.toggle()