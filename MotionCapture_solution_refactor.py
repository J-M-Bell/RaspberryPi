import os
from gpiozero import LED, MotionSensor
import time
from picamzero import Camera
import yagmail
from pathlib import Path

# set up hardware
red_led = LED(17)
pir = MotionSensor(4)
camera = Camera()
camera.still_size = (1640, 1232)

def motion_detected():
    global motionDetectedTime = time.time()
    red_led.on()
    

def motion_not_detected():
    motion_duration = time.time() - motionDetectedTime
    red_led.off()
    if motion_duration > 5.0:
        camera.take_photo(file)
    

pir.when_motion = motion_detected
pir.when_no_motion = motion_not_detected
pause()