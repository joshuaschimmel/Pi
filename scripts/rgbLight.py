import RPi.GPIO as GPIO
import hsvrgb as conv
import time

GPIO.cleanup()

# led has to be adressed as rgb, though the hsv model will be used
# in the loop so that only one loop will be needed
red = 11
green = 12
blue = 13
freq = 50
steps = 1

# setup
freq = int(input("Freq plox: "))
steps = int(input("Speed plox: "))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

# # https://en.wikipedia.org/wiki/HSL_and_HSV#From_HSV
# def HSVtoRGB(hue=0):
#     hue = int(hue)
#     # chroma is constant 100 i guess
#     c = 255
#     # some different h value
#     h = hue / 60
#     # some intermediate value x for the second largest component
#     x = round(c * (1 - abs((h % 2) -1)))
#
#
#     # yey ifs TODO dictionaries
#     if(0 <= h < 1): return (c, x, 0)
#     elif(1 <= h < 2): return (x, c, 0)
#     elif(2 <= h < 3): return (0, c, x)
#     elif(3 <= h < 4): return (0, x, c)
#     elif(4 <= h < 5): return (x, 0, c)
#     elif(5 <= h < 6): return (c, 0, x)
#     else: return (0,0,0)

r = GPIO.PWM(11, freq)
g = GPIO.PWM(12, freq)
b = GPIO.PWM(13, freq)

r.start(0)
g.start(0)
b.start(0)
try:
    while 1:
        #HSV Hue-Loop
        for hue in range(0, 360, steps):
            rgb = conv.hsvtorgb(hue)
            # rgb value needs fitting for [0,100]
            r.ChangeDutyCycle(rgb[0]/2.55)
            g.ChangeDutyCycle(rgb[1]/2.55)
            b.ChangeDutyCycle(rgb[2]/2.55)
            #sets a lower boundary for the loop speed
            time.sleep(0.1) # tweek here for speed

except KeyboardInterrupt:
    pass

r.stop()
g.stop()
b.stop()
GPIO.cleanup()
