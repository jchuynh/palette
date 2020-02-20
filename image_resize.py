## moving function into seed.py
## working file

from PIL import Image
import glob, os, sys

import model


file = "static/images//"
dirs = os.listdir(file)

def resize_image():

    size = 350, 350

    for art_image in dirs:
        if os.path.isfile(file+art_image):
            if art_image == '.DS_Store':
                 continue
            im = Image.open(file+art_image)
            im.convert('RGB')
            im.thumbnail(size, Image.ANTIALIAS)

            thumb_path = f"static/thumbnails/{ art_image }_thumb.jpg"

            im.save(thumb_path, 'JPEG', quality=80)

resize_image()