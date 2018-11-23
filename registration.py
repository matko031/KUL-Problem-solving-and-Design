import json, os
from gui import *
from facial_recognition import *
from bluetooth import *


#registration function
def registration():
    reg_gui()
    # run facial_recognition script
    face_hash = register_face()
    # send bluetooth registration signal
    # receive fingerprint hash
    fingerprint_hash = register_fingerprint()

    with open('./data.json') as json_file:
        data = json.load(json_file)

        id = str(max(data))
        data[id]["fingerprint"] = fingerprint_hash
        data[id]["face"] = face_hash

        with open('./data.json', 'w') as outfile:
            json.dump(data, outfile)

