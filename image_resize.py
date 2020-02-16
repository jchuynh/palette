import os, sys
import Image
from PIL import Image

size = 400, 400

for infile in sys.argv[1:]:
    outfile = os.path.splitest(infile)[0] + ".thumbnail"
    if infile != outfile:
