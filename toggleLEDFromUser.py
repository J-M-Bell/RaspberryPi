from gpiozero import LED
import time

led = LED(17)
user_choice = int(input("Enter 0 to turn LED off or 1 to turn LED on."))

if user_choice == 0:
    led.off()
elif user_choice == 1:
    led.on()
elif user_choice == 6:
    exit()
else:
    print("Invalid input.")
print("End")

