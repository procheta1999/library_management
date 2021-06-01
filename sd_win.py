from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from tkcalendar import DateEntry
import mysql.connector

def b():
    rt.destroy()
    import Project1

def r():
    rt.destroy()
    import rg_win
def bd():
    rt.destroy()
    import mn_win

def log():
    global e
    if e.get()=="" or p.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
     nm=e.get()
     pwd2=p.get()
     try:
        db=mysql.connector.connect(host="localhost",user="root",password="",database="books")
        mycursor=db.cursor()
        mycursor.execute("select * from student_registration where email=%s and password=%s",(nm,pwd2))
        row=mycursor.fetchone()
        if row is None:
            messagebox.showerror("Error","Invalid Email ID and Password")
        else:
          messagebox.showinfo("Success", "Successfully logged in. Welcome!")
          bd()
        db.commit()
     except EXCEPTION as e:
         print(e)
     db.rollback()
     db.close()

rt=Tk()
width= rt.winfo_screenwidth()
height= rt.winfo_screenheight()
rt.title("Students Database")
rt.geometry("%dx%d" % (width, height))
rt.maxsize(1250,550)
rt.minsize(1250,550)
bg=ImageTk.PhotoImage(file="pic2.jpg",master=rt)
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
frame1=Frame(rt,bg="white")
frame1.place(x=200,y=10,width=830,height=530)
frame2=Frame(frame1,bg="cyan")
frame2.place(x=20,y=30,width=790,height=50)
t=Label(frame2,text="Staff Login",font="Constantia 15 bold",fg="red",bg="cyan")
t.place(x=365,y=10)
frame3=Frame(frame1,bg="#f6ebeb")
frame3.place(x=20,y=110,width=790,height=400)
t1=Label(frame3,text="Email ID:",font="Constantia 15 bold",bg="#f6ebeb")
t1.place(x=300,y=100)
e=ttk.Entry(frame3,font="Constantia 15 bold")
e.place(x=300,y=130,width=250)
t6=Label(frame3,text="Password:",font="Constantia 15 bold",bg="#f6ebeb")
t6.place(x=300,y=170)
p=ttk.Entry(frame3,font="Constantia 15 bold")
p.place(x=300,y=200,width=250)
p.config(show="*")
b_1 = Button(frame3, text="Login",font="Constantia 10 bold", width='10', height='1', command=log)
b_1.place(x=300,y=270)
b_2 = Button(frame3, text="Back",font="Constantia 10 bold", width='10', height='1',command=b )
b_2.place(x=460,y=270)
b_3 = Button(frame3, text="First time user? Register first.",font="Constantia 10 bold", width='10', height='1',command=r )
b_3.place(x=300,y=340,width=250)
rt.mainloop()