from gpiozero import LED, MotionSensor
import time
from signal import pause

red_led = LED(17)
pir = MotionSensor(4)


if (pir.when_motion):
    red_led.on()
else:
    red_led.off()