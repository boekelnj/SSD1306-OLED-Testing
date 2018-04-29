# notbookies
# 4/26/18

import ssd1306
import dispTests as debug
from machine import I2C, Pin
from time import sleep

scl = Pin(12)   # Set scl and sda to GPIO pins of your choosing.
sda = Pin(13)

i2c = I2C(-1, scl, sda, freq = 400000)  # 400khz is max frequency of I2c
print(i2c.scan())   # Searches for I2c addresses on bus and prints them

# This ssd1306 object is what has to be passed to debug functions.
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.init_display()

def main():

    while True:
        display.fill(0)
        display.show()
        debug.text(display, 'This is a test of', 0, 5)
        debug.text(display, 'the .96" ssd1306', 0, 15)
        debug.text(display, 'OLED display', 0, 25)
        debug.text(display, 'with an ESP8622', 0, 35)
        debug.text(display, 'running', 0, 45)
        debug.text(display, '    MicroPython', 0, 55)
        sleep(5)
        debug.testFillV(display)
        debug.testFillH(display)
        debug.testFillRandFull(display)


if __name__ == "__main__":
    
    main()


