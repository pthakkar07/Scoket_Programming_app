import socket
from tkinter import *
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
IP = '127.0.0.1'
PORT = 1234


s.connect((HOST_NAME,PORT))

def send(listbox, entry):
    message = entry.get()
    listbox.insert('end',"Client: "+message)
    entry.delete(0,END)
    s.send(bytes(message,"utf-8"))
    receive(listbox)

def receive(listbox):
    message = s.recv(20)
    listbox.insert('end',"Server: "+message.decode('utf-8'))


root = Tk()
entry = Entry()
entry.pack(side = BOTTOM)
listbox = Listbox(root)
listbox.pack()

button = Button(root,text="Send", command = lambda : send(listbox, entry))
button.pack(side=BOTTOM)


rbutton = Button(root,text="receive", command = lambda : receive(listbox))
rbutton.pack(side=BOTTOM)

root.title("Client")

root.mainloop()