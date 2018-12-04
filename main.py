from tkinter import *
import json, threading, sys
from bluetooth import *
#from email_function import *
#from facial_recognition import *
#from registration import *
from gui import *


# now threading1 runs regardless of user input
threading1 = threading.Thread(target= lambda: bluetooth_read('/dev/rfcomm0') ) 
threading1.daemon = True
threading1.start()

main_gui()
