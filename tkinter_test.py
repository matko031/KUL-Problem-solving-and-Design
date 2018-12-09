import tkinter as tk
from tkinter import ttk, messagebox
import json, os, encryption, re, time
import email_function, authentication


WELCOME_FONT=("Verdana", 100)
LARGE_FONT = ("Verdana", 12)
background_color="papaya whip"

key = 'key.key'

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Checkin gate")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames={}

        for F in (StartPage, GDPR_welcome, SendCode, EnterCode, Register, ScanFinger, Delete, Welcome, Wanker, LearningFaces):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(100, weight=1)
            frame.grid_columnconfigure(100, weight=1)
            frame.configure(background=background_color)


        self.show_frame(StartPage)

    def show_frame(self, cont):
        string= (str(cont))


        frame = self.frames[cont]
        frame.tkraise()
        frame.update()
        event = "<<" + re.findall('(?<=\.)(.*?)(?=\')', string)[0] + ">>"
        frame.event_generate(event)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Start page", font=WELCOME_FONT, bg=background_color)
        label.grid(row=1, column=2, pady=50)

        buttons = tk.Frame(self)
        buttons.configure(background=background_color)
        buttons.grid(row=2, column=2)


        button1 = ttk.Button(buttons, text="Register", command = lambda: controller.show_frame(GDPR_welcome))
        button1.grid(row=2, column=1, padx=10)

        button2 = ttk.Button(buttons, text="SendCode", command=lambda: controller.show_frame(SendCode))
        button2.grid(row=2, column=2, padx=10)

        button3 = ttk.Button(buttons, text="EnterCode", command=lambda: controller.show_frame(EnterCode))
        button3.grid(row=2, column=3, padx=10)

        button4 = ttk.Button(buttons, text="Delete account", command=lambda: controller.show_frame(Delete))
        button4.grid(row=2, column=4, padx=10)



class SendCode(tk.Frame):

    def __init__(self, parent, controller):


        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="If you are unable to log in the usual way, please type in your email and we will send you a backup code", font=LARGE_FONT, bg=background_color)
        label.grid(row=1, column=1,columnspan=2, pady=100, sticky="N")

        email = tk.Label(self, text="Email", bg=background_color)
        email.grid(row=2, column=1, sticky="E", padx=(0,20))

        email_field = tk.Entry(self)
        email_field.grid(row=2, column=2, ipadx="100", sticky="W")

        buttons = tk.Frame(self, bg=background_color)
        buttons.grid(row=3, column=1, columnspan=2)

        submit = ttk.Button(buttons, text="Submit", command=lambda: (email_function.send_email(email_field.get(), key), email_field.delete(0, 'end'), controller.show_frame(StartPage)))
        submit.grid(row=4, column=1, padx=20, pady=40, sticky="E")

        button1 = ttk.Button(buttons, text="Main menu", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=4, column=2, padx=20, pady=40, sticky="W")



class EnterCode(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Please enter your email and the code you have received", font=LARGE_FONT, bg=background_color)
        label.grid(row=1, column=1, columnspan=2, pady=100, sticky="NE")

        email = tk.Label(self, text="Email", bg=background_color)
        email.grid(row=2, column=1, sticky="E", padx=(0,20))

        email_field = tk.Entry(self)
        email_field.grid(row=2, column=2, ipadx="100", sticky="W")

        code = tk.Label(self, text="Code", bg=background_color)
        code.grid(row=3, column=1, sticky="E", padx=(0,20), pady=10)

        code_field = tk.Entry(self)
        code_field.grid(row=3, column=2, ipadx="100", sticky="W")

        buttons = tk.Frame(self, bg=background_color)
        buttons.grid(row=4, column=1, columnspan=2)

        submit = ttk.Button(buttons, text="Submit", command= lambda: verify_code() )
        submit.grid(row=5, column=1, padx=20, pady=40, sticky="E")

        button1 = ttk.Button(buttons, text="Main menu", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=5, column=2, padx=20, pady=40, sticky="W")



        def verify_code():

            email = email_field.get()
            code = code_field.get()

            email_field.delete(0, "end")
            code_field.delete(0, "end")

            if authentication.check_code(email, code, key):
                controller.show_frame(Welcome)

            else:
                print("Go away wanker")
                controller.show_frame(Wanker)




class GDPR_welcome(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="GDPR text", font=LARGE_FONT, bg=background_color)
        label.grid(row=1, column=1, pady=100)

        buttons = tk.Frame(self, bg=background_color)
        buttons.grid(row=2, column=1)

        button1 = ttk.Button(buttons, text="Main menu", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=30)


        button2 = ttk.Button(buttons, text="Agree", command=lambda: (controller.show_frame(ScanFinger) ))
        button2.grid(row=1, column=2, padx=30)


class ScanFinger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Please scan your finger on the fingerprint sensor. Press your finger on the sensor until the red light dies out. \n Lift your finger and repeat the proccess one more time",
                         font=LARGE_FONT, bg=background_color)
        label.grid(row=1, column=1, pady=100, sticky="NE")
     
        self.bind("<<ScanFinger>>", lambda event: (time.sleep(4), controller.show_frame(Register)))


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Please enter your information in order to register", font=LARGE_FONT, bg=background_color)
        label.grid(row=1, column=1, columnspan=2, pady=100, sticky="NE")

        first_name = tk.Label(self, text="First name", bg=background_color)
        first_name.grid(row=2, column=1, sticky="E", padx=(0,20), pady=10)
        first_name_field = tk.Entry(self)
        first_name_field.grid(row=2, column=2, ipadx="100", sticky="W")

        family_name = tk.Label(self, text="Family name", bg=background_color)
        family_name.grid(row=3, column=1, sticky="E", padx=(0,20), pady=10)
        family_name_field = tk.Entry(self)
        family_name_field.grid(row=3, column=2, ipadx="100", sticky="W")

        email = tk.Label(self, text="Email", bg=background_color)
        email.grid(row=4, column=1, sticky="E", padx=(0, 20), pady=10)
        email_field = tk.Entry(self)
        email_field.grid(row=4, column=2, ipadx="100", sticky="W")


        def check_user(user_email):
            if os.path.isfile("data.json") == False:
                return True

            else:
                with open('./data.json') as json_file:
                    data = json.load(json_file)

                for id in data:
                    email = encryption.decrypt(data[id]["email"], key)
                    if user_email == email:
                        messagebox.showinfo("Repeated email", "This email already exist in our databse, please type a different email")
                        return False

                return True

        def insert():
            if (first_name_field.get() == "" or family_name_field.get() == "" or email_field.get() == ""):
                messagebox.showinfo("One of the inputs is empty", "Please fill all the fields")

            else:
                if os.path.isfile("data.json") == False:
                    data = {}

                else:
                    with open('./data.json') as json_file:
                        data = json.load(json_file)

                if len(data) == 0:
                    id = 1
                else:
                    id = int(max(data)) + 1

                if check_user(email_field.get()):

                    name = first_name_field.get()

                    customer_info = {"first_name": encryption.encrypt(name, key),
                                     "family_name": encryption.encrypt(family_name_field.get(), key),
                                     "email": encryption.encrypt(email_field.get(), key)}

                    data[id] = customer_info

                    with open('./data.json', 'w') as outfile:
                        json.dump(data, outfile)

                    controller.show_frame(LearningFaces)

                    # registration.face_registration(str(id), 5, camera)

                    # registration.learn_faces()

                    controller.show_frame(StartPage)



        buttons = tk.Frame(self, bg=background_color)
        buttons.grid(row=6, column=1, columnspan=2)

        submit = ttk.Button(buttons, text="Submit", command=insert )
        submit.grid(row=1, column=1, padx=20, pady=40, sticky="E")

        back = ttk.Button(buttons, text="Main menu", command=lambda: controller.show_frame(StartPage))
        back.grid(row=1, column=2, padx=20, pady=40, sticky="W")


class LearningFaces(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        header = tk.Label(self, text="Learning faces in progress... ",font=("Verdana", 60), bg=background_color)
        header.grid(row=1, column=1, sticky="nsew")

        label = tk.Label(self, text="A", font = LARGE_FONT, bg=background_color)
        label.grid(row=2, column=1)

        self.bind("<<LearningFaces>>", lambda event: faces_learned(label, self))

        def faces_learned(label, parent):
            for i in range(1,6):
                label['text']="Faces learned = %s/5" % (i)
                label.grid(row=2, column=1)
                label.update()
                time.sleep(3)

            label.grid_forget()
            controller.show_frame(StartPage)


class Delete(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="If you no longer wish to use are services, you can delete your account from here", font=LARGE_FONT, bg=background_color)
        label.grid(row=1, column=1, columnspan=2, pady=100, sticky="NE")

        email = tk.Label(self, text="Email", bg=background_color)
        email.grid(row=2, column=1, sticky="E", padx=(0, 20), pady=10)
        email_field = tk.Entry(self)
        email_field.grid(row=2, column=2, ipadx="100", sticky="W")



        def delete_user(user_email):
            global key

            if os.path.isfile("data.json") == False:
                no_users = True
            else:
                with open('./data.json') as json_file:
                    data = json.load(json_file)

                if len(data) == 0:
                    no_users = True
                else:
                    no_users=False

            if no_users:
                messagebox.showinfo("Empty database", "There are no registered users at the moment. Please go to the registration window in the main menu.")
                controller.show_frame(StartPage)
                return None

            else:
                if email_field.get() == "":
                    messagebox.showinfo("Empty cell", "One of the entries is empty, please fill in all the entries.")
                    return None

                authentication = False
                for id in data:
                    email = encryption.decrypt(data[id]["email"], key)
                    if email == user_email:

                        authentication = True
                        MsgBox = tk.messagebox.askquestion('Delete user', 'Are you sure you want to delete your account?', icon='warning')

                        if MsgBox == 'yes':
                            del data[id]
                            with open('./data.json', 'w') as outfile:
                                json.dump(data, outfile)

                            email_field.delete(0, "end")

                            controller.show_frame(StartPage)

                            return None

                if not authentication:
                    messagebox.showinfo("Wrong email/password", "This combination of email and password doesn't exist in our database. Please check you have typed them correctly.")



        buttons = tk.Frame(self, bg=background_color)
        buttons.grid(row=4, column=1, columnspan=2)

        submit = ttk.Button(buttons, text="Delete", command=lambda: delete_user(email_field.get()))
        submit.grid(row=5, column=1, padx=20, pady=40, sticky="E")

        button1 = ttk.Button(buttons, text="Main menu", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=5, column=2, padx=20, pady=40, sticky="W")


class Welcome(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Welcome aboard, \n dear passanger", font=("Verdana", 60), bg=background_color)
        label.grid(row=1, column=1, sticky="nsew")

        self.photo = tk.PhotoImage(file="/home/delimir/Documents/Faks/2/peno/Python/main/airplane.png")
        label = tk.Label(self, image=self.photo)
        label.grid(row=2, column=1)


class Wanker(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Go away wanker!", font=("Verdana", 60), bg=background_color)
        label.grid(row=1, column=1, sticky="nsew")

        self.bind("<<Wanker>>", lambda event: (time.sleep(6), controller.show_frame(StartPage)))




app = MainApp()
app.geometry("1280x720")
app.mainloop()