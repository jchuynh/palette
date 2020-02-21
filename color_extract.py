
from haishoku.haishoku import Haishoku
from PIL import Image
# from seed import seed.load_artworks
import requests
import sys
import json
import os # want to make a new directory/folder for each set of color palettes


img_path = "https://images.metmuseum.org/CRDImages/as/web-large/DP122117.jpg"


hai = Haishoku.loadHaishoku(img_path) 
#returns a Haishoku instance, used to read the file

palette = Haishoku.getPalette(img_path) # (percentage of color (RGB values))
# print(palette)

def new_image(mode, size, color): 
    return Image.new(mode, size, color)

def create_color_palette():
    for item in palette:
        # idx 0 is the percentage of color on the image
        c_pal = item[1] # need to keep this as a tuple, RGB color codes
        pal = new_image('RGB', (100, 100), c_pal)

        # create a new image in in RGB mode, with 100X100 px, as the RGB color

        # trying to save all color palette images in a folder named based on the artwork's title
        # folder_name = "static/color_palette/{art_title}"
        # os.makedirs(folder_name)

        file_name = f"static/color_palette/({c_pal}).jpg"
        # save the file name 
        # i += 1 # increment the file names to prevent rewriting the file
        pal.save(file_name, 'JPEG') # save color file as a jpeg    

create_color_palette()

# .ppm (Portable Pixmap) file: a 24-bit color image formatted using a text format.
# can also store the images width and height, maximum color value.
