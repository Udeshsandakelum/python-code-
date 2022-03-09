from tkinter import *
 
def addNumbers():
    res=(str(e1.get())[::-1])
    if e1.get() == res:
        res = " it is palindrome"
        myText.set(res)
    else:
        res = "it is not palindrome"
        myText.set(res)    
    

 
master = Tk()
master.geometry("270x100")
myText=StringVar()
Label(master, text="Enter a string:").grid(row=0, sticky=W)
#Label(master, text="Second").grid(row=1, sticky=W)the numbe
Label(master, text="Result:").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
#e2 = Entry(master)
 
e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)
 
b = Button(master, text="Find", command=addNumbers)
b.grid(row=6, column=0, padx=2, pady=2)
 
 
mainloop()
