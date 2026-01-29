# if motion is detected for 5 seconds on PIR then power on LED and wait 5 seconds then take a photo
#save photo to a log file

import os
from gpiozero import LED, MotionSensor
import time
from picamzero import Camera
import yagmail
from pathlib import Path
import shutil

# Set up email
password = ""
with open("/home/jmbell97/Documents/temp.txt", "r") as f:
    password = f.read().rstrip()
yag = yagmail.SMTP("justinsraspberrypi71@gmail.com", password)


# Create directory for images
new_image_dir = "/home/jmbell97/Documents/RaspberryPi/FinalProject/static/images/new"
if not os.path.exists(new_image_dir):
    os.mkdir(new_image_dir)
    

# Set up image name by finding out how many images are currently in folder
main_dir = "/home/jmbell97/Documents/RaspberryPi/FinalProject/static/images"
extension = "*.jpg"
jpg_files = list(Path(main_dir).glob(extension))
counter = len(jpg_files)
image_name = "/Image"
extension = ".jpg"
file = ""


# set up hardware
red_led = LED(17)
pir = MotionSensor(4)
camera = Camera()
camera.still_size = (1640, 1232)


try:
    while True:
        file = new_image_dir + image_name
        file += str(counter)
        file += extension
        if (pir.motion_detected):
            red_led.on()
            print("LED on. Taking a photo.")
            time.sleep(5)
            camera.take_photo(file)
            print("Photo Made. Saving photo to main folder.")
            time.sleep(1)
            try:
                shutil.copy(file, main_dir)
                print(f"File {file} is now saved to directory: {main_dir}")
                time.sleep(2)
            except Exception as e:
                print(f"An error occurred {e}")
                time.sleep(2)
            print("Sending Email Now.")
            time.sleep(2)
            subject = "Image " + str(counter)
            contents = "This is Image Number: " + str(counter)
            yag.send(to="justinmbell1997@gmail.com",
                     subject=subject,
                     contents=contents,
                     attachments=file)
            print("Email sent")
            time.sleep(2)
            counter += 1        
        else:
            red_led.off()
            print("LED off")
except KeyboardInterrupt:
    pass
