from tkinter import *
from tkinter import messagebox
import cv2
import webbrowser
import winsound
root = Tk()

root.geometry("290x500")
root.title("Lock ((alone)) by Sula")
root.iconbitmap("lock.ico")
root.resizable(False,False)
root.attributes("-alpha",0.9)

title = Label(root,text="Screen Lock",bg="#D82148",fg="white",font=("Stencil",21))
title.pack(fill=X)

f1 = Frame(root,bg="white")
f1.place(x = 0, y = 38,width=298,height=460)



title1 = Label(f1,text="Enter Password",fg="black",bg = "white",font=("Stencil",20))
title1.place(x = 47,y=10)



En1 = Entry(root,justify=CENTER,font=("impact",25),fg="#D82148",bd=2,relief=RIDGE,width=10,bg="white")
En1.place(x = 50,y=80)







def one(event = None):
    one = 1
    En1.insert(END,one)
def one2(event = None):
    two = 2
    En1.insert(END,two)
def one3(event = None):
    three= 3
    En1.insert(END,three)
def one4(event = None):
    four = 4
    En1.insert(END,four)
def one5(event = None):
    Five = 5
    En1.insert(END,Five)
def one6(event = None):
    six = 6
    En1.insert(END,six)
def one7(event = None):
    Seven = 7
    En1.insert(END,Seven )
def one8(event = None):
    eight= 8
    En1.insert(END,eight)
def one9(event = None):
    nine= 9
    En1.insert(END,nine)
def one0(event = None):
    zero= 0
    En1.insert(END,zero)







def reset(event = None):
    En1.delete("0",END)
    l2.place(x = 990000,y = 332683)
    l3.place(x = 990000,y = 332683)

def ok(event = None):
    Password = En1.get()
    if Password == "2010":
        global l3
        l3 = Label(root,text="correct Password",font=("Stencil",10),bg="white",fg="#1BEC48")
        l3.place(x = 80,y = 130)
        messagebox.showinfo("Welcome","correct Password")
        root.destroy()
        root2 = Tk()
        root2.geometry("540x590")
        root2.title("Social Media programs [by Suliman]")
        root2.resizable(False,False)


        def insta(event = None):
            webbrowser.open("www.instagram.com")
            
        def twit(event = None):
            webbrowser.open("www.twitter.com")
            
        def Face(event = None):
            webbrowser.open("www.Facebook.com")
            
        def Snap(event = None):
            webbrowser.open("www.Snapchat.com")
            
        def You(event = None):
            webbrowser.open("www.youtube.com")
            


        butt = Button(root2,text="instagram",
                compound=BOTTOM,
                fg="red",
                bg="white",
                bd=2,
                width=10,
                height=3,
                font=("stencil",25),
                command=insta)
        butt.place(x = 300,y = 30)
        butt = Button(root2,text="twitter",
                compound=BOTTOM,
                fg="red",
                bg="white",
                bd=2,
                width=10,
                height=3,
                font=("stencil",25),
                command=twit)
        butt.place(x = 20,y = 30)
        butt = Button(root2,
                text="Facebook",
                compound=BOTTOM,
                fg="red",
                bg="white",
                bd=2,
                width=10,
                height=3,
                font=("stencil",25),
                command=Face)
        butt.place(x = 300,y = 200)
        butt = Button(root2,
                text="Snapchat",
                compound=BOTTOM,
                fg="red",
                bg="white",
                bd=2,
                width=10,
                height=3,
                font=("stencil",25),
                command=Snap)
        butt.place(x = 20,y = 200)
        butt = Button(root2,
                text="Youtube",
                compound=BOTTOM,
                fg="red",
                bg="white",
                bd=2,
                width=10,
                height=3,
                font=("stencil",25),
                command=You)
        butt.place(x = 170,y = 370)

        root.mainloop()
    else:
        global l2
        l2 = Label(root,text="incorrect Password",font=("Stencil",10),bg="white",fg="#D82148")
        l2.place(x = 80,y = 130)
        s = cv2.VideoCapture(0)
        ret,image = s.read()
        cv2.imwrite("thief1.png",image)
        del(s)
        messagebox.showerror("Error","incorrect Password")
        winsound.Beep(2000,32767)



b1 = Button(f1,text="1",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one)
b1.place(x = 20,y = 155)

b2 = Button(f1,text="2",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one2)
b2.place(x = 110,y = 155)
b3 = Button(f1,text="3",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one3)
b3.place(x = 200,y = 155)
b4 = Button(f1,text="4",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one4)
b4.place(x = 20,y = 225)
b5 = Button(f1,text="5",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one5)
b5.place(x = 110,y = 225)
b6 = Button(f1,text="6",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one6)
b6.place(x = 200,y = 225)
b7 = Button(f1,text="7",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one7)
b7.place(x = 20,y = 295)
b8 = Button(f1,text="8",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one8)
b8.place(x = 110,y = 295)
b9 = Button(f1,text="9",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one9)
b9.place(x = 200,y = 295)
b0 = Button(f1,text="0",
            font=("stencil",25),
            bg = "white",
            bd=0 ,
            relief=GROOVE,
            width=3,
            cursor="hand2",
            command=one0
            )
b0.place(x = 110,y = 370)

bok = Button(f1,text="✔",
            fg="green",
            bg ="white",
            bd=0,
            font=("Stencil",25),
            command=ok)
bok.place(x = 200,y = 370)

bx = Button(f1,text="❌",fg="red",bd=0,bg="white",font=("Stencil",25),command=reset)
bx.place(x = 20,y=370)




root.mainloop()