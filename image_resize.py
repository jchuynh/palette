## moving function into seed.py
## working file

from PIL import Image
import glob, os

size = 350, 350


file = "static/images/DT1567.jpg"
thumb_path = f"static/thumbnails/test.jpg"

def resize_image():
    im = Image.open(file)
    im.convert('RGB')
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(thumb_path, 'JPEG', quality=80)
