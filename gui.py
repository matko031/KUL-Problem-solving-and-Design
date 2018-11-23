from tkinter import *
from email_function import *
import os.path, json

def switch_windows(window):
    root.destroy()
    window()

def auth_gui():
    global root

    root = Tk()

    # set the backgroud color of GUI window
    root.configure(background='light green')

    # set the title of the GUI window
    root.title('authentication form')

    # set the configuration of the GUI window
    root.geometry("500x300")

    # create a text
    auth = Label(root, text="AUTHENTICATING", fg="red", background="light green")
    auth.place(relx=.5, rely=.5, anchor="center")
    auth.config(font=("Courier", 44))

    #create button to send email
    send_email_button=Button(root, text="send email code", fg="Black", bg="light gray", command= lambda: switch_windows(email_send_gui))
    send_email_button.pack()

    auth_email_button = Button(root, text="enter email code", fg="Black", bg="light gray", command=lambda: switch_windows(email_auth_gui))
    auth_email_button.pack()

    reg_button = Button(root, text="register", fg="Black", bg="light gray", command=lambda: switch_windows(reg_gui))
    reg_button.pack()

    root.mainloop()

    # start the GUI

    root.mainloop()

def reg_gui():
    global root

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
            customer_info = {"first_name": first_name_field.get(), "family_name": family_name_field.get(),
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

        root.destroy()



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
    email = Label(root, text="Email", bg="light green")


    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    first_name.grid(row=1, column=0)
    family_name.grid(row=2, column=0)
    email.grid(row=3, column=0)

    # create a text entry box
    # for typing the information
    first_name_field = Entry(root)
    family_name_field = Entry(root)
    email_field = Entry(root)

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
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=insert)
    submit.grid(row=8, column=1)

    # start the GUI
    root.mainloop()

def email_send_gui():
    global root

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

def email_auth_gui():
    global root

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


auth_gui()