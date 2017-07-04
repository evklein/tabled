import sys 
import random as rand
import time
from neopixel import *

LED_COUNT = 30
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.WS2811_STRIP_GRB

def wheel(pos):
    if pos < 85:
	return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
	pos -= 85
	return Color(255 - pos * 3, 0, pos * 3)
    else:
	pos -= 170
	return Color(0, pos * 3, 255 - pos * 3)

def run_color_scheme(scheme, statics = [], wait = 50):
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    strip.begin()
    if scheme == 'STATUS-FLASH':
	for i in range(0, 10, 1):
	    for j in range(strip.numPixels()):
	        strip.setPixelColor(j, Color(0, 0, 0))
	    strip.show()
	    time.sleep(500 / 1000.0)
	    for j in range(strip.numPixels()):
		strip.setPixelColor(j, Color(0, 50, 180))
	    strip.show()
	    time.sleep(500 / 1000.0)
	
    if scheme == 'STATIC-ONE-COLOR':
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(statics[0], statics[1], statics[2]))
	strip.show()
    elif scheme == 'STATIC-TWO-COLOR':
	for i in range(0, strip.numPixels(), 2):
	    strip.setPixelColor(i, Color(statics[0], statics[1], statics[2]))
	    strip.setPixelColor(i + 1, Color(statics[3], statics[4], statics[5]))
	strip.show()
    elif scheme == 'STATIC-THREE-COLOR':
	for i in range(0, strip.numPixels(), 3):
	    strip.setPixelColor(i, Color(statics[0], statics[1], statics[2]))
	    strip.setPixelColor(i + 1, Color(statics[3], statics[4], statics[5]))
	    strip.setPixelColor(i + 2, Color(statics[6], statics[7], statics[8]))
	strip.show()
    elif scheme == 'CHASE':
	while True:
	    for q in range(3):
		for i in range(0, strip.numPixels(), 3):
		    strip.setPixelColor(i + q, Color(statics[0], statics[1], statics[2]))
		strip.show()
		time.sleep(wait / 1000.0)
		for i in range(0, strip.numPixels(), 3):
		    strip.setPixelColor(i + q, 0)
    elif scheme == 'ROTATE-TWO-COLOR':
        first = Color(statics[0], statics[1], statics[2])
	second = Color(statics[3], statics[4], statics[5])
	while True:
	    for i in range(0, strip.numPixels(), 2):
		strip.setPixelColor(i, first)
		strip.setPixelColor(i + 1, second)
            strip.show()
	    time.sleep(wait / 1000.0)
	    temp = first
	    first = second
	    second = temp
    elif scheme == 'ROTATE-THREE-COLOR':
        first = Color(statics[0], statics[1], statics[2])
	second = Color(statics[3], statics[4], statics[5])
	third = Color(statics[6], statics[7], statics[8])
	while True:
	    for i in range(0, strip.numPixels(), 3):
		strip.setPixelColor(i, first)
		strip.setPixelColor(i + 1, second)
		strip.setPixelColor(i + 2, third)
            strip.show()
	    time.sleep(wait / 1000.0)
	    temp = first
	    first = second
	    second = third
	    third = temp
    elif scheme == 'ROTATE-FOUR-COLOR':
	first = Color(statics[0], statics[1], statics[2])
	second = Color(statics[3], statics[4], statics[5])
	third = Color(statics[6], statics[7], statics[8])
	fourth = Color(statics[9], statics[10], statics[11])
	while True:
	    for i in range(0, strip.numPixels(), 4):
		strip.setPixelColor(i, first)
		strip.setPixelColor(i + 1, second)
		strip.setPixelColor(i + 2, third)
		strip.setPixelColor(i + 3, fourth)
            strip.show()
	    time.sleep(wait / 1000.0)
	    temp = first
	    first = second
	    second = third
	    third = fourth
	    fourth = temp
    elif scheme == 'STACK':
	first = Color(statics[0], statics[1], statics[2])
	second = Color(statics[3], statics[4], statics[5])
	for i in range(strip.numPixels()):
	    strip.setPixelColor(i, first)
            strip.show()
	while True:
	    for i in range(strip.numPixels()):
		for j in range(strip.numPixels() - 1, -1, -1):
		    strip.setPixelColor(j, second)
		    strip.setPixelColor(j + 1, first)
		    if j == i:
			strip.setPixelColor(i, second)
			strip.show()
			time.sleep(wait / 1000.0)
		        break
		    strip.show()
		    time.sleep(wait / 1000.0)
	    temp = first
	    first = second
            second = temp
    elif scheme == 'STACK-MIDDLE':
	first = Color(statics[0], statics[1], statics[2])
	second = Color(statics[3], statics[4], statics[5])
	for i in range(strip.numPixels()):
	    strip.setPixelColor(i, first)
	    strip.show()
	while True:
	    for i in range(strip.numPixels()):
		reverse = 1
		for j in range((strip.numPixels() / 2) - 1, -1, 1):
		    strip.setPixelColor(j, second)
		    strip.setPixelColor(j + 1, first)
		    strip.setPixelColor(j - reverse, second)
		    strip.setPixelColor(j - reverse - 1, first)
		    if j == i:
			strip.setPixelColor(i, second)
			strip.setPixelColor(i - reverse, second)
		        strip.show()
			time.sleep(wait / 1000.0)
	    temp = first
	    first = second
	    second = temp
    elif scheme == 'RAINBOW':
	j = 0
	while True:
	    j += 1
	    for i in range(strip.numPixels()):
		strip.setPixelColor(i, wheel((i + j) & 255))
	    strip.show()
	    time.sleep(wait / 1000.0)
    elif scheme == 'RAINBOW-CYCLE':
	j = 0
	while True:
	    j += 1
	    for i in range(strip.numPixels()):
		strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
	    strip.show()
	    time.sleep(wait / 1000.0)
    elif scheme == 'GREATEST-GODDAMN-COUNTRY':
	run_color_scheme('ROTATE-THREE-COLOR', wait=200, statics=[255, 0, 0, 255, 255, 255, 0, 0, 255])
    elif scheme == 'HALLOWEEN':
	run_color_scheme('ROTATE-TWO-COLOR', wait=200, statics=[220, 20, 0, 0, 255, 0])
    elif scheme == 'CHRISTMAS':
	run_color_scheme('ROTATE-THREE-COLOR', wait=200, statics=[255, 0, 0, 255, 255, 255, 0, 255, 0])
    elif scheme == 'ST-PATRICKS':
	run_color_scheme('ROTATE-TWO-COLOR', wait=200, statics=[255, 255, 255, 0, 255, 0])
    elif scheme == 'GO-COLTS':
	run_color_scheme('ROTATE-TWO-COLOR', wait=200, statics=[0, 40, 220, 255, 255, 255])
    elif scheme == 'HAIL-PURDUE':
	run_color_scheme('ROTATE-TWO-COLOR', wait=200, statics=[255, 140, 0, 255, 255, 255])
    elif scheme =='SEIZURE-MODE':
	while True:
	    for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255)))
	    strip.show()
	    time.sleep(50 / 1000.0)
    elif scheme == 'SHUTDOWN':
	for i in range(strip.numPixels()):
	    strip.setPixelColor(i, Color(0, 0, 0))
	strip.show()
    elif scheme == 'SCHEMES' or scheme == 'MANUAL':
	show_schemes()

def show_schemes():
	print '''
    Scheme                   | Description                                                                      | Parameters
    -------------------------+----------------------------------------------------------------------------------+-----------------------------------
    static-one-color         | Show one color consistently across all pixels.                                   | 3 RGB values
    static-two-color         | Show two colors consistently across all pixels (alternating).                    | 6 RGB values
    static-three-color       | Show three colors consistently across all pixels (alternating).                  | 9 RGB values
    rotating-two-color       | Show two colors rotating across pixels.                                          | Wait (milliseconds), 6 RGB values
    rotating-three-color     | Show three colors rotating across pixels.                                        | Wait (milliseconds), 9 RGB values
    rotating-four-color      | Show four colors rotating across pixels.                                         | Wait (milliseconds), 12 RGB values
    chase                    | Show one color chasing after itself.                                             | Wait (milliseconds), 3 RGB values
    rotate-two-colors        | Show two colors rotating around the strip (alternating).                         | Wait (milliseconds), 6 RGB values
    rotate-three-colors      | Show three colors rotating around the strip (alternating).                       | Wait (milliseconds), 9 RGB values
    rotate-four-colors       | Show four colors rotating around the strip (alternating).                        | Wait (milliseconds), 12 RGB values
    stack                    | Show two colors, one stacking on top of another, until they switch.              | Wait (milliseconds), 6 RGB values
    stack-middle             | Show two colors, one stacking on top of another from the middle until switching. | Wait (milliseconds), 6 RGB values
    rainbow                  | Rotate rainbow colors consistently on each pixel.                                | Wait (milliseconds)
    rainbow-cycle            | Rotate rainbow colors across different pixels evenly.                            | Wait (milliseconds)
    sexy                     | Mood lighting, for getting her nice and bothered ;)                              | Wait (milliseconds)
    greatest-goddamn-country | 4th of July celebration colors.                                                  | Wait (milliseconds)
    halloween                | Halloween celebration colors.                                                    | -
    christmas                | Christmas celebration colors.                                                    | -
    st-patricks              | St. Patrick's Day celebration colors.                                            | -
    go-colts                 | Colts colors.                                                                    | -
    hail-purdue              | Purdue colors.                                                                   | -
    seizure-mode             | Flashes random colors on random intervals very quickly (not for epilleptics).    | - 
    shutdown                 | Turn off all pixels.                                                             | -
    schemes/manual           | Show all color schemes                                                           | -
      '''

num_args = len(sys.argv)

try:
    if num_args == 2:
        run_color_scheme(scheme=sys.argv[1].upper())
    elif num_args == 3:
        run_color_scheme(scheme=sys.argv[1].upper(), wait=float(sys.argv[2]))
    elif num_args >= 4:
        run_color_scheme(scheme=sys.argv[1].upper(), wait=float(sys.argv[2]), statics=map(int, sys.argv[3:]))
except KeyboardInterrupt:
    print "\nStopping scheme."
    sys.exit(2)
