
def read_list_met_obj():
    """Read the object ids from a txt file."""

    met_obj_list = []

    # opens and reads text file of met object endpoints
    with open("art_obj_id.txt", "r") as obj_file:
        for line in obj_file:
            new_line = line.rstrip()
            met_obj_list.append(new_line)

    return met_obj_list # returns met object list as items in an array


def search_through_url(met_list):
    """Add the JSON data into a list."""

    met_json_list = []

    for met_obj in met_list:

        # add the object list into the Met Museusm's API URL
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{met_obj}"
        response = requests.get(url)
        json_data = response.json()

        # Add each JSON file associated with the object into a list
        met_json_list.append(json_data)

    return met_json_list