
from PIL import Image
import seed
import glob, os

size = 350, 350


file = "static/images/DT1494.jpg"
thumb_path = f"static/thumbnails/test2.jpg"

im = Image.open(file)
im.convert('RGB')
im.thumbnail(size, Image.ANTIALIAS)
im.save(thumb_path, 'JPEG', quality=80)
