import json
from facial_recognition import *

def auth_fun(id):

    id=str(id)
    with open('./data.json') as json_file:  # open the json file
        data = json.load(json_file)

    if id in data:
        facehash = register_face()
        if facehash == data[id]["face"]:
            print("Welcome")

        else:
            print("Go away")

    else:
        print("Please register first \n")

    print("Finished")





