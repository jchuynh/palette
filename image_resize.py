import glob, os, sys
import Image
from PIL import Image

size = 400, 400

infile = "static/images/DT1494.jpg"

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitest(infile)
    im = Image.open(infile)
    im.tumbnail(size)
    im.save(file + ".thumbnail","JPEG")
