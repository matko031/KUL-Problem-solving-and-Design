from tkinter import *
from bluetooth import *
import threading

def switch_loops():
    global root1

    root1.destroy()
    test2()

# now threading1 runs regardless of user input
threading1 = threading.Thread(target=listen_bluetooth)
threading1.daemon = True
threading1.start()



def test1():
    global root1

    root1 = Tk()

    # set the backgroud color of GUI window
    root1.configure(background='light green')

    # set the title of the GUI window
    root1.title('authentication form')

    # set the configuration of the GUI window
    root1.geometry("500x300")

    # create a text

    auth = Label(root1, text="AUTHENTICATING", fg="red", background="light green")
    auth.place(relx=.5, rely=.5, anchor="center")
    auth.config(font=("Courier", 44))

    submit=Button(root1, text="Submit", fg="Black", bg="Red", command=switch_loops)
    submit.pack()

    # start the GUI

    root1.mainloop()



def test2():
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

    root.mainloop()



test1()
