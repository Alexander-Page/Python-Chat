import socket
from Tkinter import *
import threading

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
MESSAGE = "Hello, World!"
SERVER = (UDP_IP, 5005)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


def recieve_thread():

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        message = "Clinet 2: " + data + "\n"
        output.insert(END, message)
        output.yview('scroll', '1', 'pages')

def click(event=None):
    entered_text = textentry.get()
    sock.sendto(entered_text, SERVER)
    textentry.delete(0, END)


window = Tk()
window.title("Client 1")
window.geometry('675x230+200+200')


labelText = StringVar()
labelText.set("Chat Client")
label1 = Label(window, textvariable=labelText, height=4)
label1.grid(row=0, column=0, sticky=W)

textentry = Entry(window, width=98, bg="white")
textentry.grid(row=2, column=0, sticky=W)

Button(window, text="Submit", width=6, command=click) .grid(row=2, column=1, sticky=W)
window.bind('<Return>',click)

output = Text(window, width=80, height=6, wrap=WORD, background="white")
output.grid(row=1, column=0, columnspan=2, sticky=W)

scrollb = Scrollbar(window, command=output.yview)
scrollb.grid(row=1, column=2, rowspan=2, ipady=25, sticky=NW)


rec_thread = threading.Thread(target=recieve_thread)
rec_thread.setDaemon(True)
rec_thread.start()
window.mainloop()

