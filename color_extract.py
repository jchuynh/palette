
from haishoku.haishoku import Haishoku
from PIL import Image
from model import Artwork, connect_to_db, db
import requests
import json
import os # want to make a new directory/folder for each set of color palettes



img_path = "https://collectionapi.metmuseum.org/public/collection/v1/objects/436530"

hai = Haishoku.loadHaishoku(img_path) 
#returns a Haishoku instance, used to read the file

palette = Haishoku.getPalette(img_path) # (percentage of color (RGB values))
# print(palette)

def new_image(mode, size, color): 
    return Image.new(mode, size, color)


for item in palette:
    # idx 0 is the percentage of color on the image
    c_pal = item[1] # need to keep this as a tuple, RGB color codes
    pal = new_image('RGB', (100, 100), c_pal)
    # create a new image in in RGB mode, with 100X100 px, as the RGB color

    folder_name = "static/color_palette/{art_title}"

    os.makedirs(folder_name)

    file_name = f"static/color_palette/({c_pal}).jpg"
    # save the file name 
    # i += 1 # increment the file names to prevent rewriting the file
    pal.save(file_name, 'JPEG') # save color file as a jpeg    


# .ppm (Portable Pixmap) file: a 24-bit color image formatted using a text format.
# can also store the images width and height, maximum color value.
