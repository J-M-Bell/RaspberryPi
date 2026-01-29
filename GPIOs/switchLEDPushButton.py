from gpiozero import LED, Button
import time
from signal import pause

red_led = LED(17)
blue_led = LED(27)
green_led = LED(22)

leds = [red_led, blue_led, green_led]

button = Button(26, bounce_time = 0.05)

counter = 0

def turnOffLEDs():
    for i in range(len(leds)):
        leds[i].off()

def switch_leds():
    global counter
    turnOffLEDs()
    counter += 1
    if counter >= len(leds):
        counter = 0
    leds[counter].on()

turnOffLEDs()
button.when_pressed = switch_leds
pause()
        