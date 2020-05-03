#!/usr/bin/env python
import time
import RPi.GPIO as GPIO

from datetime import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=False)
device.contrast(16)
        
def countdown_timer():
    
    t = 75

    while t:
        hours, minutes = divmod(t, 60)
        
        if hours < 10:
            hours = "0" + str(hours)
            
        if minutes < 10:
            minutes = "0" + str(minutes)
        
        with canvas(device) as draw:
            text(draw, (0, 1), str(hours), fill="white", font=proportional(CP437_FONT))
            text(draw, (15, 1), ":", fill="white", font=proportional(TINY_FONT))
            text(draw, (17, 1), str(minutes), fill="white", font=proportional(CP437_FONT))
        time.sleep(1)
        t -= 1
        
def main():
    
    countdown_timer()

if __name__ == "__main__":
    main()
