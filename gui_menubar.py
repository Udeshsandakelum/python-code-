#from cProfile import label
from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import colorchooser
import os
#__________________________________________________________________________________________________________

def colourmode():
    
    color = colorchooser.askcolor()
    y = color[1]

x = y

root = Tk(className="udesh")
root.configure(bg = "black")
root.geometry("800x420")
TextArea = scrolledtext.ScrolledText(root , font=x)
TextArea.pack(expand=True,fill=BOTH)
file = None
#________________________________________________________________________________________________________
# create menu
MenuBar = Menu(root)
root.config(menu=MenuBar)
# configure File and Edit menus with MenuBar
FileMenu = Menu(MenuBar , tearoff=0)
EditMenu = Menu(MenuBar , tearoff=0)
AboutMenu = Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="File",menu=FileMenu)
MenuBar.add_cascade(label="Edit",menu=EditMenu)
MenuBar.add_cascade(label = "About",menu=AboutMenu)
#_______________________________________________________________________________________________________
# functions for File and Edit menus
#_______________________________________________________________________________________________________
def about():
    win = Tk()
    win.geometry()
    mainloop()

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
EditMenu.add_command(label = "Cut"  )
EditMenu.add_command(label = "Copy" )
EditMenu.add_command(label = "Paste")
EditMenu.add_command(label = "Bg colour",command=colourmode)

AboutMenu.add_command(label = "about",command=about)
root.mainloop()
