#import facial_recognition
import encryption, datetime, json, os
from dateutil import parser


def authentication(id):

    id = str(id)

    with open('./data.json') as json_file:
        data = json.load(json_file)

    if id in data:
        #face = facial_recognition.check_face()

        name = encryption.decrypt(data[id]["first_name"], 'key.key')

        if name == face:
            print("Welcome")

        else:
            print("Go away, wanker")

    else:
        print("Please register first \n")

    print("Finished")


def check_code(email, code, key):

    if os.path.isfile("data.json") != False:

        with open('./data.json') as json_file:
            data = json.load(json_file)


        for id in data:
            if email == encryption.decrypt(data[id]["email"], key):
                if data[id].get("code") != None and data[id].get("code_timestamp") != None:
                    if  code == encryption.decrypt(data[id].get("code"), key) \
                            and ( (parser.parse(encryption.decrypt(data[id].get("code_timestamp"), key)) - datetime.datetime.now()).total_seconds() )/3600 <= 1.0:

                        del data[id]["code"]
                        del data[id]["code_timestamp"]

                        with open('./data.json', 'w') as outfile:
                            json.dump(data, outfile)

                        return True

    return False