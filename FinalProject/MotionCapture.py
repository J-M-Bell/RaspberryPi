import os
from gpiozero import LED, MotionSensor
import time
from picamzero import Camera
import yagmail
from pathlib import Path


# Set up image name by finding out how many images are currently in folder
main_dir = "/home/jmbell97/Documents/RaspberryPi/FinalProject/img"
if not os.path.exists(main_dir):
    os.mkdir(main_dir)
new_image_file = "/home/jmbell97/Documents/RaspberryPi/FinalProject/photo_logs.txt"
extension = "*.jpg"
jpg_files = list(Path(main_dir).glob(extension))
image_name = "/img_"
extension = ".jpg"
file = ""

lastTimeMotionDetected = time.time()
lastTimePhotoTaken = time.time()
motionDetectDelay = 5.0
takePhotoDelay = 30.0

# set up hardware
red_led = LED(17)
pir = MotionSensor(4)
camera = Camera()
camera.still_size = (1640, 1232)


class MotionCapture(): 

    def __init__(self):
        """
        constructor for MotionCapture class
        
        :param self: MotionCapture - The MotionCapture object
        """
        self.remove_txt_file()

    def take_photo(file):
        """
        A method that takes a photo with the camera and saves it.
        
        :param file: String - the filepath that the photo is saved to.
        """
        camera.take_photo(file)
        print("Photo Made. Saving photo to main folder.")
        
        
    def write_to_txt_file(file):
        """
        A method that stores the filepath of a new image in
        a log text file.
        
        :param file: String - filepath of the new image
        """
        if not os.path.exists(new_image_file):
            with open(new_image_file, 'a') as opened_file:
                opened_file.write(f"{file}\n")
        print(f"File saved as: {file}")


    def remove_txt_file(file):
        """
        A method that deletes the image storage text 
        file if it does exist. 
        
        :param file: String - filepath for images
        """
        if os.path.exists(file):
            os.remove(file)


    def send_photo_by_email(file):
        # Set up email
        password = ""
        with open("/home/jmbell97/Documents/temp.txt", "r") as f:
            password = f.read().rstrip()
        yag = yagmail.SMTP("justinsraspberrypi71@gmail.com", password)
        time.sleep(2)
        subject = "New Image"
        contents = "Image: " + file
        yag.send(to="justinmbell1997@gmail.com",
                    subject=subject,
                    contents=contents,
                    attachments=file)
        print("Email sent")
        time.sleep(2)

photo_taker = MotionCapture()

try:
    while True:
        #created file string
        now = time.time() 
        image_name += str(now)
        image_name += extension
        file = main_dir + image_name
        if (now - lastTimePhotoTaken > takePhotoDelay):
            if (pir.motion_detected):
                # turn LED on
                red_led.on()
                if (now - lastTimeMotionDetected > motionDetectDelay):
                    # take photo
                    print("LED on. Taking a photo.")
                    photo_taker.take_photo(file)
                    photo_taker.write_to_txt_file(file)
                    lastTimeMotionDetected += now

                    # send email with new photo attached
                    print("Sending Email Now.")
                    photo_taker.send_photo_by_email(image_name)    
            else:
                red_led.off()
except KeyboardInterrupt:
    pass
