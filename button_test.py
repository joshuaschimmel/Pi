#import RPi.GPIO as GPIO
import time
import board
import neopixel

# set mode as BCM and turn warnings off
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)


# use BCM 24 for input
#GPIO.setup(24, GPIO.IN)

# neopixel settings
num_pixels = 60
# BCM pin for pixel strip
pixel_pin = board.D18
ORDER = neopixel.GRB
step = 32
wait = 0.5

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2,
                           auto_write=False, pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


def rainbow_full(wait):
    for j in range(255):
        pixels.fill(wheel(j))
        pixels.show()
        time.sleep(wait)



i = 0
# loop
while 1:
    i = i % 255
    # check if input is on
    #if GPIO.input(24) == GPIO.LOW:
        # change color
    #    print("Button pressed!")
    #    i += step
    pixels.fill(wheel(i))
    pixels.show()
    time.sleep(wait)

