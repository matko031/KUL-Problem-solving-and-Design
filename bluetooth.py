import time
"""
address = "00:0E:0E:0D:7B:08"
serverMACAddress = address
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
s.close()
"""

def register_fingerprint():
    return "123456"


def listen_bluetooth():
    while True:
        print( "Listening to bluetooth")
        time.sleep(1)