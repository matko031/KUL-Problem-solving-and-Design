import re, random, json, datetime, smtplib, os.path
from tkinter import *


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

def send_email_gui():
    if os.path.isfile("data.json") == False :
        data={}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)


    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("Bypass code")

    # set the configuration of GUI window
    root.geometry("500x300")

    # create a Form label
    heading = Label(root, text="Bypass form", bg="light green")

    # create an email label
    email = Label(root, text="Email", bg="light green")




    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    email.grid(row=1, column=0)

    # create a text entry box
    # for typing the information
    email_field = Entry(root)

    # bind method of widget is used for
    # the binding the function with the events





    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    email_field.grid(row=1, column=1, ipadx="100")


    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black", bg="Red", command= lambda: (send_email(email_field.get()), root.destroy() ) )
    submit.grid(row=8, column=1)

    # start the GUI
    root.mainloop()

def email_auth():
    if os.path.isfile("data.json") == False :
        data={}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

    # Function to set focus (cursor)
    def focus1(event):
        # set focus on the course_field box
        code_field.focus_set()



    # Function for clearing the
    # contents of text entry boxes
    def clear():
        # clear the content of text entry box
        email_field.delete(0, END)
        code_field.delete(0, END)

    # Function to take data from GUI
    # window and write to an excel file
    def validate_email_code():
        # if user not fill any entry
        # then print "empty input"

        email_input=email_field.get()
        code_input=code_field.get()

        with open('./data.json') as json_file:
            data = json.load(json_file)


        email_in_database=False

        for id in data:
            if email_input == data[id]["email"]:
                if "code" in data[id]:
                    if data[id]["code"] == str(code_input):
                        print("Welcome %s %s" % (data[id]["first_name"], data[id]["family_name"]))
                        del data[id]["code"]
                        del data[id]["code_timestamp"]
                        email_in_database = True


        if email_in_database == False:
            print("This email is not recognised in our database")

        with open('./data.json', 'w') as outfile:
            json.dump(data, outfile)


        # call the clear() function
        clear()

        root.destroy()



    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("Bypass code")

    # set the configuration of GUI window
    root.geometry("500x300")

    # create a Form label
    heading = Label(root, text="Bypass form", bg="light green")

    # create an email label
    email = Label(root, text="Email", bg="light green")

    # create a code label
    code = Label(root, text="Code", bg="light green")


    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    email.grid(row=1, column=0)
    code.grid(row=2, column=0)

    # create a text entry box
    # for typing the information
    email_field = Entry(root)
    code_field = Entry(root)

    # bind method of widget is used for
    # the binding the function with the events

    # whenever the enter key is pressed
    # then call the focus1 function
    email_field.bind("<Return>", focus1)



    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    email_field.grid(row=1, column=1, ipadx="100")
    code_field.grid(row=2, column=1, ipadx="100")


    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black", bg="Red", command=validate_email_code)
    submit.grid(row=8, column=1)

    # start the GUI
    root.mainloop()




