from tkinter import *
from email_function import *
from authentication import *
import registration
import os.path, json



def switch_windows(current, new):
    current.destroy()
    new()

def main_gui():

    global root_main

    root_main = Tk()

    # set the backgroud color of GUI window
    root_main.configure(background='light green')

    # set the title of the GUI window
    root_main.title('authentication form')

    # set the configuration of the GUI window
    root_main.geometry("500x300")

    # create a text
    auth = Label(root_main, text="WELCOME", fg="red", background="light green")
    auth.place(relx=.5, rely=.5, anchor="center")
    auth.config(font=("Courier", 150))

    #create button to send email
    send_email_button=Button(root_main, text="send email code", fg="Black", bg="light gray", command= lambda: switch_windows(root_main, email_send_gui))
    send_email_button.place(relx=.35, rely=.8, anchor="center")
    send_email_button.config(font=("Courier", 20))

    auth_email_button = Button(root_main, text="enter email code", fg="Black", bg="light gray", command=lambda: switch_windows(root_main, email_auth_gui))
    auth_email_button.place(relx=.65, rely=.8, anchor="center")
    auth_email_button.config(font=("Courier", 20))

    reg_button = Button(root_main, text="register", fg="Black", bg="light gray", command=lambda: switch_windows(root_main, reg_gui))
    reg_button.place(relx=.5, rely=.8, anchor="center")
    reg_button.config(font=("Courier", 20))

    # start the GUI

    root_main.mainloop()

def reg_gui():


    if os.path.isfile("data.json") == False :
        data={}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

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
        insert()

    # Function for clearing the
    # contents of text entry boxes
    def clear():
        # clear the content of text entry box
        first_name_field.delete(0, END)
        family_name_field.delete(0, END)
        email_field.delete(0, END)


    # Function to take data from GUI
    # window and write to an excel file
    def insert():
        # if user not fill any entry
        # then print "empty input"

        if (first_name_field.get() == "" or
            family_name_field.get() == "" or
            email_field.get() == ""):

            print("empty input")

        else:
            name = first_name_field.get()
            customer_info = {"first_name": name, "family_name": family_name_field.get(),
                             "email": email_field.get()}

            with open('./data.json') as json_file:
                data = json.load(json_file)

            if len(data) == 0:
                data[1] = customer_info

            else:
                id = int(max(data)) + 1
                data[id] = customer_info

            with open('./data.json', 'w') as outfile:
                json.dump(data, outfile)

            # set focus on the name_field box
            first_name_field.focus_set()

            # call the clear() function
            clear()

        
        registration.face_registration(name, 5)
        
        registration.learn_faces()
        
        print("learned")

        switch_windows(root_reg, main_gui)

    global root_reg

    # create a GUI window
    root_reg = Tk()

    # set the background colour of GUI window
    root_reg.configure(background='light green')

    # set the title of GUI window
    root_reg.title("registration form")

    # set the configuration of GUI window
    root_reg.geometry("500x300")

    # create a Form label
    heading = Label(root_reg, text="Registration form", bg="light green")

    # create a first name label
    first_name = Label(root_reg, text="First name", bg="light green")

    # create a family name label
    family_name = Label(root_reg, text="Family name", bg="light green")

    # create an email label
    email = Label(root_reg, text="Email", bg="light green")


    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    first_name.grid(row=1, column=0)
    family_name.grid(row=2, column=0)
    email.grid(row=3, column=0)

    # create a text entry box
    # for typing the information
    first_name_field = Entry(root_reg)
    family_name_field = Entry(root_reg)
    email_field = Entry(root_reg)

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


    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    first_name_field.grid(row=1, column=1, ipadx="100")
    family_name_field.grid(row=2, column=1, ipadx="100")
    email_field.grid(row=3, column=1, ipadx="100")

    # create a Submit Button and place into the root window
    submit = Button(root_reg, text="Submit", fg="Black", bg="Red", command=insert)
    submit.grid(row=8, column=1)

    back = Button(root_reg, text="<--", fg="Black", bg="Red", command= lambda: switch_windows(root_reg, main_gui) )
    back.grid(row=9, column=1)


    # start the GUI
    root_reg.mainloop()

def email_send_gui():
    global root_email_send

    if os.path.isfile("data.json") == False :
        data={}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)


    # create a GUI window
    root_email_send = Tk()

    # set the background colour of GUI window 
    root_email_send.configure(background='light green')

    # set the title of GUI window
    root_email_send.title("Bypass code")

    # set the configuration of GUI window
    root_email_send.geometry("500x300")

    # create a Form label
    heading = Label(root_email_send, text="Bypass form", bg="light green")

    # create an email label
    email = Label(root_email_send, text="Email", bg="light green")




    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    email.grid(row=1, column=0)

    # create a text entry box
    # for typing the information
    email_field = Entry(root_email_send)

    # bind method of widget is used for
    # the binding the function with the events





    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    email_field.grid(row=1, column=1, ipadx="100")


    # create a Submit Button and place into the root window
    submit = Button(root_email_send, text="Submit", fg="Black", bg="Red", command= lambda: (send_email(email_field.get()), switch_windows(root_email_send, root_main) ) )
    submit.grid(row=8, column=1)

    back = Button(root_email_send, text="<--", fg="Black", bg="Red", command=lambda: switch_windows(root_email_send, main_gui))
    back.grid(row=9, column=1)

    # start the GUI
    root_email_send.mainloop()

def email_auth_gui():
    global root_email_auth

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

        root_email_auth.destroy()



    # create a GUI window
    root_email_auth = Tk()

    # set the background colour of GUI window
    root_email_auth.configure(background='light green')

    # set the title of GUI window
    root_email_auth.title("Bypass code")

    # set the configuration of GUI window
    root_email_auth.geometry("500x300")

    # create a Form label
    heading = Label(root_email_auth, text="Bypass form", bg="light green")

    # create an email label
    email = Label(root_email_auth, text="Email", bg="light green")

    # create a code label
    code = Label(root_email_auth, text="Code", bg="light green")


    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    email.grid(row=1, column=0)
    code.grid(row=2, column=0)

    # create a text entry box
    # for typing the information
    email_field = Entry(root_email_auth)
    code_field = Entry(root_email_auth)

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
    submit = Button(root_email_auth, text="Submit", fg="Black", bg="Red", command=validate_email_code)
    submit.grid(row=8, column=1)

    back = Button(root_email_auth, text="<--", fg="Black", bg="Red", command=lambda: switch_windows(root_email_auth, main_gui))
    back.grid(row=9, column=1)

    # start the GUI
    root_email_auth.mainloop()

