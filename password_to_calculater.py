
from tkinter import*
from tkinter import messagebox
win=Tk()
win.title("udesh")
win.resizable(0,0)
win.geometry('190x130')
win.configure(background='white')
label = Label(win,fg='black',bg='white',text='Enter your password to ').pack()
label2 = Label(win, fg='black',bg='white',text='run the this software').pack()
text='1'

#display = " "

#add_text = StringVar()


 

def textprint():
    global text
    #global display
    add_text = StringVar()
    display = " "
    
    
    
    if text==ent.get():
        root = Tk()
        root.geometry('312x344')
        root.resizable(0,0)
        root.title("udesh'calculater")
        #global display 

        #add_text = StringVar()
        #global add_text
        

        def btnclick(num):
            #display= " "
            global display
            display = display + str(num)
            add_text.set(display)

        def btnclear(): 

            global display
            #display = " " 
            add_text.set(display)

        def bt_equal():
            global display
            #display = " "
            result = str(eval(display))
            add_text.set(result)

        
        input_frame = Frame(root, width=312, height=50,  highlightbackground="green", highlightcolor="green", highlightthickness=6)
        input_frame.pack(side=TOP)
        input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=  add_text, width=50, bg="white", bd=0,justify=RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = Frame(root, width=312, height=272.5, bg="black")
        btns_frame.pack()

        #first row
        clear = Button(btns_frame,text='c',fg='red',width=32,height=3,bg='black',command = lambda:btnclear())
        devide = Button(btns_frame,text='/',fg='red',width=10,height=3,bg='black',command =  lambda:btnclick('/'))

        seven = Button(btns_frame,text='7',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(7))
        eight = Button(btns_frame,text='8',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(8))
        nine = Button(btns_frame,text='9',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(9))
        multiply = Button(btns_frame,text='*',fg='red',width=10,height=3,bg='black',command = lambda:btnclick('*'))
        #third row
        four = Button(btns_frame,text='4',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(4))
        five = Button(btns_frame,text='5',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(5))
        six = Button(btns_frame,text='6',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(6))
        minus = Button(btns_frame,text='-',fg='red',width=10,height=3,bg='black',command = lambda:btnclick('-'))
        #fourth row

        one = Button(btns_frame,text='1',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(1))
        two = Button(btns_frame,text='2',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(2))
        three = Button(btns_frame,text='3',fg='red',width=10,height=3,bg='black',command = lambda:btnclick(3))
        plus = Button(btns_frame,text='+',fg='red',width=10,height=3,bg='black',command = lambda:btnclick('+'))
        #fifth row

        zero = Button(btns_frame,text='0',fg='red',width=21,height=3,bg='black',command = lambda:btnclick(0))
        point = Button(btns_frame,text='.',fg='red',width=10,height=3,bg='black',command = lambda:btnclick('.'))
        equal = Button(btns_frame,text='=',fg='red',width=10,height=3,bg='black',command = lambda:bt_equal())
        #place the clear and devide buttons


        clear.grid(row=0,column=0,columnspan=3)
        devide.grid(row=0,column=3)
        #place the seven,eight,nine and multiply buttons

        seven.grid(row=1,column=0)
        eight.grid(row=1,column=1)
        nine.grid(row=1,column=2)
        multiply.grid(row=1,column=3)
        #place the four,five,six and minus buttons

        four.grid(row=2,column=0)
        five.grid(row=2,column=1)
        six.grid(row=2,column=2)
        minus.grid(row=2,column=3)
        #place the  one,two,three and plus buttons

        one.grid(row=3,column=0)
        two.grid(row=3,column=1)
        three.grid(row=3,column=2)
        plus.grid(row=3,column=3)
        #place the zero,point and equal butons

        zero.grid(row=4,column=0,columnspan=2)
        point.grid(row=4,column=2)
        equal.grid(row=4,column=3)

        root.mainloop()


        
       

    else:
        messagebox.showwarning("Error password","plese try again")
        
         
         
def   Exit():
        win.destroy()
        exit()         


        
        
       

ent=Entry(bg='red',fg='black',bd=5,justify='left',selectbackground='yellow',selectforeground='green',width=40,cursor='')


ent.pack()
btn1=Button(win,text='Log in',command=textprint).pack()
btn1=Button(win,text='Exit',width=5,height=1,command=Exit).pack()





win.mainloop()


