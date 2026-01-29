import os
from flask import Flask, render_template
from exif import Image
from pathlib import Path
from datetime import datetime, date

main_dir = "/home/jmbell97/Documents/RaspberryPi/FinalProject/static/images"
replacement = "/home/jmbell97/Documents/RaspberryPi/FinalProject"
latest_file_replacement = "/home/jmbell97/Documents/RaspberryPi/FinalProject/static/images/Image"
new_img_dir = "/home/jmbell97/Documents/RaspberryPi/FinalProject/static/images/new"
extension = "*.jpg"
    
def getLatestImage():
    # Get count of all images
    jpg_files = list(Path(main_dir).glob(extension))
    count = len(jpg_files) - 1
    count_characters = len(str(count))
    print(f"Latest image number: {count}")
    latest_file = ''
    for file in jpg_files:
        filepath = str(file)
        print(f"The file path is: {filepath}")
        new_file = filepath.replace(latest_file_replacement, "")
        print(f"The replacement is: {new_file}")
        print(f"file number search: {new_file[0:count_characters]}")
        if new_file[0:count_characters] == str(count):
            latest_file = str(file)
#     latest_file = jpg_files[len(jpg_files)-1]
#     image_path = str(latest_file)
    image_path = latest_file.replace(replacement, "")
    print(f"The final image path: {image_path}")
    return image_path

def getNewImageCount(): 
    # Get count of new images
    new_images = list(Path(new_img_dir).glob(extension))
    new_img_count = len(new_images)
    return new_img_count
    
def clearNewImageFolder():
    new_images = list(Path(new_img_dir).glob(extension))
    for image in new_images:
        try:
            os.remove(image)
            print(f"Removed path: {image}") 
        except Exception as e:
            print(f"An error occurred {e}")
    
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello From Flask"

@app.route("/check-photos")
def check_photos():
    # add check in this function to check to see if a new photo has been added to list
    image_path = getLatestImage()
    new_img_count = getNewImageCount()
    clearNewImageFolder()
    return render_template('index.html', image_path=image_path, new_img_count=new_img_count)
        
app.run(host="0.0.0.0", port=8500)    