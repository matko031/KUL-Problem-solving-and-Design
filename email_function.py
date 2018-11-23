import random, json, datetime, smtplib, os.path


def send_email(email):


    with open('./data.json') as json_file:  #open the json file
        data = json.load(json_file)

    # ask the user for it's email address and use regex to check that the email address is in correct format
    #######   -> still have to figure out how to pass this to tkinter   ######

    """
    email_correct = False
    while email_correct==False:
        email=input("Please type your email address ")
        if re.match('^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', email):
            email_correct = True
        else:
            print("This is not a valid email address, please type in a valid address")
    """

    code = str(random.randint(10000, 99999)) #create the code with which the user can log in

    timestamp=str(datetime.datetime.now()) #timestamp of the code


    for entry in data:
        if data[entry]["email"] == email:
            data[entry]["code"]=code
            data[entry]["code_timestamp"]=timestamp
            name = data[entry]["first_name"]
            surname = data[entry]["family_name"]

            #send the email

            sender = "peno3iot@gmail.com"
            recipient = email
            password = "wastebasket"  # Your SMTP password for Gmail
            subject = "Bypass code"
            text = "Dear %s %s, \n you have recently requested a code to pass our security system. \n If you haven't requested this code, please" \
                   "ignore this code, otherwise, here is the code %s " % (name, surname, code)

            smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            smtp_server.login(sender, password)
            message = "Subject: {}\n\n{}".format(subject, text)
            smtp_server.sendmail(sender, recipient, message)
            smtp_server.close()



    with open('./data.json', 'w') as outfile:
        json.dump(data, outfile)







