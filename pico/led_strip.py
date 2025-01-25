from machine import Pin
import time
from neopixel import NeoPixel



class LED_STRIP:
    
    off: bool = False
    strip: Neopixel = None
    color: [int. int, int] = None  # rgb
    brightness: float = 1 # [0,1]
    
    def __init__(self, pin: int, n_pixels: int):
        self.strip = NeoPixel(Pin(pin), n_pixels)
        self.off = False
    
    def _check_rgb_range(self, c: int):
        return min(max(0, c), 255)
    
    def set_color(self, r: int, g: int, b: int):
        self.color = [
            self._check_rgb_range(r),
            self._check_rgb_range(g),
            self._check_rgb_range(b),
        ]
        self.off = False
        return self
    
    
    def set_off(self):
        self.off = True
        return self
    
    def set_brightness(self, brightness_percentage: float):
        self.brightness = min(max(0, brightness_percentage), 1)
        return self

    def update(self):
        if self.off:
            self.strip.fill((0, 0, 0))
        else:
            
            self.strip.fill((
                round(self.color[0] * self.brightness),
                round(self.color[1] * self.brightness),
                round(self.color[2] * self.brightness)
            ))
            
        self.strip.write()


if __name__ == "__main__":
    strip = LED_STRIP(0, 20)
    strip.set_color(255, 191, 0).update()

    time.sleep(5)
    strip.set_off().update()
    del strip
