from tkinter import *
from tkinter  import messagebox
import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbol = string.punctuation
all = lower + upper + symbol
temp = random.sample(all,k=6)
password = "".join(temp)
text = password
#define function
def addNumbers():
    global text
    if text == str(e1.get()):
        win = Tk()
        Label(win,text="Thank you\nFor run this software!!").pack()
        win.mainloop()
    else:
        messagebox.askretrycancel("tk","Try again\n\n Please enter correct password")
#Driver code
#Create the window
master = Tk()
master.geometry("250x100")
Label(master, text="Enter the name:").grid(row=1, sticky=W)
Label(master, text="Enter the password:").grid(row=2, sticky=W)
e1 = Entry(master)
e2 = Entry(master)
e2.grid(row=2,column=1) 
e1.grid(row=1, column=1) 
b = Button(master, text="Log in", command=addNumbers)
b.grid(row=7,sticky=W)
mainloop()
