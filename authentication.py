import json
from facial_recognition import *


def authentication(id):

    id = str(id)

    with open('./data.json') as json_file:  # open the json file
        data = json.load(json_file)



    if id in data:
        print("id in data - authentication.py")
        name = check_face()

        
        if name == data[id]["first_name"]:
            print("Welcome")

        else:
            print("Go away, wanker")

    else:
        print("Please register first \n")

    print("Finished")


