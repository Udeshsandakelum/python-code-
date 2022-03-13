#
from tkinter import *

chunk_tax = 0
Interest_Rate = 0#guhjgjifjijfijjf
#defing a function as add number
def Income_tax():
    global chunk_tax
    global Interest_Rate
    input1=int(e1.get())#)+int(e2.get())
    relevant = input1 - 500000
    part = relevant - (relevant % 500000)
    chunk = int(part / 500000)
    for i in range(1,int(chunk + 1)):
        Interest_Rate += 4 
        Amount_tax = 500000 * (Interest_Rate/100)
        chunk_tax += Amount_tax
    other_tax = (relevant%500000) * ((Interest_Rate +4 )/100)
    myText.set(other_tax + chunk_tax)
#Create the window 
master = Tk()
myText=StringVar()
#Create two labels
Label(master, text="Enter your income of this year:").grid(row=0, sticky=W)
Label(master, text="You should pay Rs :").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
#Use the entry box to input and output 
e1 = Entry(master)
e2 = Entry(master)
#Place the entry box 
e1.grid(row=0, column=1)
#Create a button to calculate the income tax 
b = Button(master, text="Calculate", command=Income_tax)
b.grid(row=4, column=0, padx=5, pady=5)
#Mainloop() function  
mainloop()
