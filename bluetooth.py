from authentication import *
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
                if int(newstr[index+1:]) >= 0:
                    id=int(newstr[0:index])
                    print(id)
                    ok = True
            except:
                print("Something went wrong, loooolz")
                ok = False
            
            if ok == True:
                print("a")
                authentication(id)
                print("b")

def bluetooth_send(message, channel):
    ser = serial.Serial(port=str(channel), baudrate = 9600, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, timeout = 1)
    counter = 0
    while counter < 5:
        counter += 1
        time.sleep(2)
        ser.write(bytes(str(message), 'utf-8'))
