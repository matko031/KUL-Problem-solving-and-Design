from tkinter import *
import json, threading, sys
import bluetooth
#from email_function import *
#from facial_recognition import *
#from registration import *
import gui


# now threading1 runs regardless of user input
threading1 = threading.Thread(target= lambda: bluetooth.bluetooth_read('/dev/rfcomm0') )
threading1.daemon = True
threading1.start()

gui.main_gui()
