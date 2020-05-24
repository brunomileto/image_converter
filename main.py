# Give two parameters, the folder that exists, and the second param will be the name of a new folder I want to create
from PIL import Image
import os
import glob

# Grab the first and second argument
# check if new folder exists, if not create it
# Loop through input_directory folder and convert images to png
# Save all pictures in the new folder

input_folder = input('Inform the path or name of the input directory: ').strip()  # Grab the first argument
input_folder = input_folder + '/'
output_folder = input('Inform the path or name of the output directory: ').strip()    # Grab the second argument
output_folder = output_folder + '/'

input_image_type = input('Inform the type of the input images: ').strip()
output_image_type = input('Inform the output of the images: ').strip()

try:    # Error handler
    os.mkdir('./' + output_folder)  # mkdir will try to create the new folder. If it exists, it will raises an error
except FileExistsError:     # If exists, it will raises this error so, we can just ignoring it as the path exist already
    pass

for file in glob.glob(input_folder + '*.' + input_image_type):  # glob will get the path of each file that matches the
    # rule inside ()
    img = Image.open(file)
    img_name = img.filename.replace(input_folder, '')
    img.save(output_folder + '/' + img_name + '.' + output_image_type, output_image_type.upper())

