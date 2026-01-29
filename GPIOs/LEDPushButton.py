from gpiozero import LED, Button
import time
from signal import pause

led = LED(17)
button = Button(26)

button.when_pressed = led.on
button.when_released = led.off

pause()



