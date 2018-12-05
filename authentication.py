import json
import facial_recognition
import encryption


def authentication(id):

    id = str(id)

    with open('./data.json') as json_file:  # open the json file
        data = json.load(json_file)



    if id in data:
        face = facial_recognition.check_face()

        name = encryption.decrypt(data[id]["first_name"], 'key.key')

        if name == face:
            print("Welcome")

        else:
            print("Go away, wanker")

    else:
        print("Please register first \n")

    print("Finished")


