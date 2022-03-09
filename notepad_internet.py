from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
#__________________________________________________________________________________________________________
root = Tk()
root.title("udesh notepad")
root.geometry("500x500")
TextArea = scrolledtext.ScrolledText(root , font="lucida 13")
TextArea.pack(expand=True,fill=BOTH)
file = None
#________________________________________________________________________________________________________
# create menu
MenuBar = Menu(root)
root.config(menu=MenuBar)
# configure File and Edit menus with MenuBar
FileMenu = Menu(MenuBar , tearoff=0)
EditMenu = Menu(MenuBar , tearoff=0)
MenuBar.add_cascade(label="File",menu=FileMenu)
MenuBar.add_cascade(label="Edit",menu=EditMenu)
#_______________________________________________________________________________________________________
# functions for File and Edit menus
def newFile():
    global file
    root.title("Untitled - Notepad")
    TextArea.delete(1.0,END)
#_________________________________________________________________________________________________________    
def openFile():
    global file
    file = askopenfilename(defaultextension =".txt",filetypes=[("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        #TextArea.delete(1.0, END)
        f = open(file,"r")
        #f.write(TextArea.get(1.0,END))
        TextArea.insert(1.0, f.read())
        f.close()
#__________________________________________________________________________________________________________        
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension =".txt",filetypes=[("All Files","*.*"),
        ("Text Documents","*.txt"),("HTML document","*.html")])
        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad ")
    else:
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
#__________________________________________________________________________________________________________        
def exitFile():
    root.destroy()
    
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
#________________________________________________________________________________________________________    
# adding new, open, and save file functionality to File menu
FileMenu.add_command(label="New" , command = newFile)
FileMenu.add_command(label="Open" , command = openFile)
FileMenu.add_command(label="Save" , command = saveFile)
# separator inside File menus
FileMenu.add_separator()
# adding exit function to File menu
FileMenu.add_command(label = "Exit" , command = exitFile)
# adding cut, copy, paste functionalities to Edit menu
EditMenu.add_command(label = "Cut" , command = cut)
EditMenu.add_command(label = "Copy" , command = copy)
EditMenu.add_command(label = "Paste" , command = paste)
root.mainloop()
