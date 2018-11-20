# import tkinter module
from tkinter import *
import json


# Function to set focus (cursor)
def focus1(event):
    # set focus on the course_field box
    family_name_field.focus_set()


# Function to set focus
def focus2(event):
    # set focus on the sem_field box
    email_field.focus_set()


# Function to set focus
def focus3(event):
    # set focus on the form_no_field box
    gsm_field.focus_set()




# Function for clearing the
# contents of text entry boxes
def clear():
    # clear the content of text entry box
    first_name_field.delete(0, END)
    family_name_field.delete(0, END)
    email_field.delete(0, END)
    gsm_field.delete(0, END)


# Function to take data from GUI
# window and write to an excel file
def insert():
    # if user not fill any entry
    # then print "empty input"


    if (first_name_field.get() == "" and
        family_name_field.get() == "" and
        sem_field.get() == "" and
        form_no_field.get() == "" and
        contact_no_field.get() == "" and
        email_id_field.get() == "" and
        address_field.get() == ""):

        print("empty input")

    else:
        customer_info = {"first_name": first_name_field.get(), "family_name":  family_name_field.get(), "email": email_field.get(), "gsm": gsm_field.get()}

        with open('./data.json') as json_file:
            data = json.load(json_file)

        if len(data)==0:
            data[1]= customer_info

        else:
            id=int(max(data))+1
            data[int(id)] = customer_info

        with open('./data.json', 'w') as outfile:
            json.dump(data, outfile)

        # set focus on the name_field box
        first_name_field.focus_set()

        # call the clear() function
        clear()





if __name__ == "__main__":
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("registration form")

    # set the configuration of GUI window
    root.geometry("500x300")


    # create a Form label
    heading = Label(root, text="Registration form", bg="light green")

    # create a first name label
    first_name = Label(root, text="First name", bg="light green")

    # create a family name label
    family_name = Label(root, text="Family name", bg="light green")

    # create an email label
    email = Label(root, text="email", bg="light green")

    # create a GSM label
    gsm = Label(root, text="GSM", bg="light green")



    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    first_name.grid(row=1, column=0)
    family_name.grid(row=2, column=0)
    email.grid(row=3, column=0)
    gsm.grid(row=4, column=0)

    # create a text entry box
    # for typing the information
    first_name_field = Entry(root)
    family_name_field = Entry(root)
    email_field = Entry(root)
    gsm_field = Entry(root)

    # bind method of widget is used for
    # the binding the function with the events

    # whenever the enter key is pressed
    # then call the focus1 function
    first_name_field.bind("<Return>", focus1)

    # whenever the enter key is pressed
    # then call the focus2 function
    family_name_field.bind("<Return>", focus2)

    # whenever the enter key is pressed
    # then call the focus3 function
    email_field.bind("<Return>", focus3)

    # whenever the enter key is pressed
    # then call the focus4 function
    gsm_field.bind("<Return>", focus3)


    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    first_name_field.grid(row=1, column=1, ipadx="100")
    family_name_field.grid(row=2, column=1, ipadx="100")
    email_field.grid(row=3, column=1, ipadx="100")
    gsm_field.grid(row=4, column=1, ipadx="100")


    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=insert)
    submit.grid(row=8, column=1)

    # start the GUI
    root.mainloop()