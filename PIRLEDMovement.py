from gpiozero import LED, MotionSensor
import time
from signal import pause



red_led = LED(17)
pir = MotionSensor(4)

while True:
    pir.when_motion = red_led.on
    pir.when_no_motion = red_led.off