from exif import Image
from pathlib import Path
from datetime import datetime, date

with open("/home/jmbell97/Documents/RaspberryPi/FinalProject/log/Image0.jpg", "rb") as image_file:
    my_image = Image(image_file)
    
if my_image.has_exif:
    print(f"Image contains {len(dir(my_image))} EXIF tags.")
    
for tag in dir(my_image):
    print(f"Tag: {tag} and Value: {my_image.get(tag)}.")
    
directory = "/home/jmbell97/Documents/RaspberryPi/FinalProject/log"
extension = "*.jpg"

jpg_files = list(Path(directory).glob(extension))
print(jpg_files)

# for file in jpg_files:
#     with open(file, "rb") as image_file:
#         my_image = Image(image_file)
#         if my_image.has_exif:
#             timestamp = my_image.get("datetime")
#             iamge_date = datetime.strptime(timestamp, "%Y-%m-%d-"
            