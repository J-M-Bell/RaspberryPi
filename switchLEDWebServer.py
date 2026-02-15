from flask import Flask
from gpiozero import LED

app = Flask(__name__)

red_led = LED(17)
blue_led = LED(27)
green_led = LED(22)

leds = [red_led, blue_led, green_led]


@app.route("/")
def index():
    return "Hello From Flask"


@app.route("/led/<int:led_number>/state/<int:state>")
def switch_led(led_number, state):
    if led_number < 0 or led_number > len(leds):
        return "Wrong LED number: " + str(led_number)
    if state != 0 and state != 1:
        return "State must be either 0 or 1"
    if state == 0:
        leds[led_number].off()
        return "LED " + str(led_number) + " is off"
    else:
        leds[led_number].on()
        return "LED " + str(led_number) + " is on"
    return "Done"

app.run(host="0.0.0.0", port=8500)
            
        
    
