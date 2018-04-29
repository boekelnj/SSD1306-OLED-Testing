# notbookies
# 4/26/18
# Test functions for testing an ssd1306 display (128x64 px) on the esp8266
# Input parameter must be an SSD1306_I2C object

from time import sleep
import urandom

# Fills the entire display one vertical line at a time, from left to right
def testFillV(display):
    display.fill(0)
    display.show()
    for x in range(0, 128):
        display.vline(x, 0, 64, 1)
        display.show()   

# Fills the entire display one horizontal line at a time, from top to bottom        
def testFillH(display):
    display.fill(0)
    display.show()
    for y in range(0, 64):
        display.hline(0, y, 128, 1)
        display.show()

# Fills the screen in groups of 32 pixels.
# Runs exactly 256 times, random fill and does not target empty pixels.
def testFillRand(display):
    display.fill(0)
    display.show()
    
    for i in range(0, 256):
        for j in range(0, 33):
            x = urandom.getrandbits(7)
            y = urandom.getrandbits(6)
            display.pixel(x, y, 1)
        display.show()

# Fills the screen in groups of 32 pixels.
# Run exactly 256 times, but only picks pixels that are off.
# Much more likely to fill entire screen, but slower.   
def testFillRandFull(display):
    display.fill(0)
    display.show()
    
    for i in range(0, 256):
        for j in range(0, 33):
            x = urandom.getrandbits(7)
            y = urandom.getrandbits(6)
            z = 0
            while display.pixel(x, y) == 1 and z < 250:
                x = urandom.getrandbits(7)
                y = urandom.getrandbits(6)
                z += 1
            display.pixel(x, y, 1)
                
        display.show()

# Displays string at specific coordinates.        
def text(display, string='test123', x=0, y=0):
    display.text(string, x, y)
    display.show()
    sleep(2)
