#from authentication import *
import time
import serial

def bluetooth_read(channel):
    print("bluetooth started")
    while True:
        ser = serial.Serial(port=str(channel), baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, timeout = 1)
        read = str(ser.readline())
        newstr = read[2:len(read)-5]
        
               
        if len(newstr) != 0:
            print(newstr)
            try:
                index = newstr.index("x")
                if int(newstr[index+1:]) >= 150:
                    id=int(newstr[0:index])
                    print(id)
                    authentication(id)
            except:
                print("Something went wrong")
        
 
bluetooth_read('/dev/rfcomm0')
