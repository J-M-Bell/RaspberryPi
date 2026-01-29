import os
from picamzero import Camera
import time

filepath = "/home/jmbell97/Documents/images"
if not os.path.exists(filepath):
    os.mkdir(filepath)
    
camera = Camera()
camera.still_size = (1640, 1232)

counter = 0
image_name = "/Image"
extension = ".jpg"
file = ""
try:
    while True:
        file = filepath + image_name
        file += str(counter)
        file += extension 
        camera.take_photo(file)
        counter += 1
        time.sleep(5)
        print("Photo Made")
except KeyboardInterrupt:
    pass

# camera.capture_sequence(file, num_images=10, interval=5)
print("End")
