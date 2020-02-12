
from haishoku.haishoku import Haishoku
from PIL import Image
import requests
import json


##### TESTING COLOR EXTRACTION #####

def new_image(mode, size, color):  # need to take into account percentage
    return Image.new(mode, size, color)


palette = Haishoku.getPalette('DT1567.jpg')
print(palette) #prints percentage of color and RGB values

Haishoku.showPalette('DT1567.jpg')

h = Haishoku.loadHaishoku('DT1567.jpg')

# pal = new_image('RGB', (100, 100), h.showPal)
# pal.save("test.jpg", "JPEG")


# .ppm (Portable Pixmap) file: a 24-bit color image formatted using a text format.
# can also store the images width and height, maximum color value.



##### API #####



url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/489064'


response = requests.get(url)
data = response.json()

data.loads()

# JSON.dumps dumos it back into a dictionary

# JSON.loads loading it in? returns an obj

# payload = {'title': art_title,
#            'artistDisplayName': artist_name,
#            'classification': art_media_code,
#            'primaryImageSmall': art_image}

print(data)




# @app.route('/')
# def hompage():
#     """Displays homepage."""

#     return render_template('homepage.html')



