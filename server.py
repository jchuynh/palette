
from haishoku.haishoku import Haishoku
import haishoku.haillow
from PIL import Image
import requests
import json



##### API #####



# url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'


# response = requests.get(url)
# data = response.json()

# objects = json.dumps(data)

# for idx, val in enumerate(objects):
#     if val = 
        



# payload = {'title': art_title,
#            'artistDisplayName': artist_name,
#            'classification': art_media_code,
#            'primaryImageSmall': art_image}




##### TESTING COLOR EXTRACTION #####

img_path = 'https://images.metmuseum.org/CRDImages/ep/web-large/DT1567.jpg'

hai = Haishoku.loadHaishoku(img_path) 
#returns a Haishoku instance, used to read the file

palette = Haishoku.getPalette(img_path) # (percentage of color (RGB values))
# print(palette)

def new_image(mode, size, color):
    return Image.new(mode, size, color)

i = 1
for item in palette:
    # idx 0 is the percentage of color on the image
    c_pal = item[1] # need to keep this as a tuple, RGB color codes
    pal = new_image('RGB', (100, 100), c_pal)
    # create a new image in in RGB mode, with 100X100 px, as the RGB color
    file_name = f"static/color_palette/test{i}.jpg"
    # save the file name 
    i += 1 # increment the file names to prevent rewriting the file
    pal.save(file_name, 'JPEG') # save color file as a jpeg    


# .ppm (Portable Pixmap) file: a 24-bit color image formatted using a text format.
# can also store the images width and height, maximum color value.






# @app.route('/')
# def hompage():
#     """Displays homepage."""

#     return render_template('homepage.html')



