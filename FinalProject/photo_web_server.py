import os
from flask import Flask, render_template
from exif import Image
from pathlib import Path
from datetime import datetime, date

# file paths
main_dir = "/home/jmbell97/Documents/RaspberryPi/FinalProject/static/img"
replacement = "/home/jmbell97/Documents/RaspberryPi/FinalProject"
latest_file_replacement = "/home/jmbell97/Documents/RaspberryPi/FinalProject/static/img/img_"
new_img_dir = "/home/jmbell97/Documents/RaspberryPi/FinalProject/static/images/new"
extension = "*.jpg"


# def getLatestImage():
#     """
#     A method that gets the latest image in the iamge directory.

#     :return the String of the file path of the latest image
#     """
#     # Get count of all images
#     jpg_files = list(Path(main_dir).glob(extension))
#     count = len(jpg_files) - 1
#     count_characters = len(str(count))
#     print(f"Latest image number: {count}")
#     latest_file = ''
#     for file in jpg_files:
#         filepath = str(file)
#         print(f"The file path is: {filepath}")
#         new_file = filepath.replace(latest_file_replacement, "")
#         print(f"The replacement is: {new_file}")
#         print(f"file number search: {new_file[0:count_characters]}")
#         if new_file[0:count_characters] == str(count):
#             latest_file = str(file)
# #     latest_file = jpg_files[len(jpg_files)-1]
# #     image_path = str(latest_file)
#     image_path = latest_file.replace(replacement, "")
#     print(f"The final image path: {image_path}")
#     return image_path


def getLatestImagePath(): 
    """
    A method that gets the latest image in the image directory.

    :return String - filepath of latest image
    """
    # Get count of new images
    all_images = list(Path(main_dir).glob(extension))
    all_images.sort()
    all_images_count = len(all_images)
    latest_image_path = all_images[all_images_count-1]
    latest_image = str(latest_image_path)
    return latest_image

def getTextFileCount():
    """
    A method that scans the photo storage text file for the 
    number of files.

    :return int - number of new images
    """
    txt_filepath = "/home/jmbell97/Documents/RaspberryPi/FinalProject/photo_logs.txt"
    counter = 0
    if os.path.exists(txt_filepath):
        with open(txt_filepath, 'r') as opened_file:
            for line in opened_file:
                print(line)
                counter += 1
        os.remove(txt_filepath)
    return counter


app = Flask(__name__)

@app.route("/")
def index():
    """
    A function that renders the text "Hello From Flask".
    """
    return "Hello From Flask"

@app.route("/check-photos")
def check_photos():
    """
    A function that uses the image file functions to render the latest image
    and update the state of whether there are new images since the last refresh.
    """
    complete_image_path = getLatestImagePath()
    new_img_count = getTextFileCount()
    display_image_path = complete_image_path.replace(replacement, "")
    return render_template('index.html', image_path=complete_image_path, new_img_count=new_img_count, display_image_path=display_image_path)
        
app.run(host="0.0.0.0", port=8500)    