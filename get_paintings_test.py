
import requests
import json

search_paintings = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=Paintings"
response = requests.get(search_paintings)
data = response.json()

for item in data:
    painting_objs = item[1]

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/{ }"

for obj_id in painting_objs:
    open("https://collectionapi.metmuseum.org/public/collection/v1/objects/{ obj_id }")

# key, val = data
# paintings_objs = dict((key, data[key]))
# for key in ["objectIDs"]:
#     if key in data:
#         print(paintings_objs)
        



