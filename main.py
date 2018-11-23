from tkinter import *
import json, threading, sys
from bluetooth import *
from email_function import *
from facial_recognition import *
from registration import *
from gui import *
from getch import *



# now threading1 runs regardless of user input
threading1 = threading.Thread(target=listen_bluetooth)
threading1.daemon = True
threading1.start()


#authentication function
def auth_fun():
    True




while True:
    getch=Getch()
    key=getch()

    if key == "r":
        registration()

    elif key == "m":
        email_send_gui()

    elif key=="n":
        email_auth_gui()

    elif key=="q":
        sys.exit()

    else:
        auth_fun()

