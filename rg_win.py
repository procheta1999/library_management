from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def b():
    rt.destroy()
    import Project1

def reg():
    if fn.get()=="" or ln.get()=="" or cn.get()=="" or ei.get()==""or cal.get()=="" or pa.get()=="" or cp.get()=="":
        messagebox.showerror("Error","All fields are required.")
    elif pa.get()!=cp.get():
        messagebox.showerror("Error", "Password and confirm password must match.")
    elif vag.get()==0:
        messagebox.showerror("Error", "Please agree to our terms and conditions.")
    else:
         nm=fn.get()
         lm=ln.get()
         cont1=cn.get()
         e=ei.get()
         dob1=cal.get()
         password1=pa.get()
         cpass=cp.get()
         db=mysql.connector.connect(host="localhost",user="root",password="",database="books")
         mycursor=db.cursor()
         try:
            sql="insert into student_registration(first_name,last_name,contact_no,email,birthday,password)values(%s,%s,%s,%s,%s,%s)"
            val=(nm,lm,cont1,e,dob1,password1)
            mycursor.execute(sql,val)
            db.commit()
            lastid=mycursor.lastrowid
            messagebox.showinfo("information","Record Inserted successfully")
            fn.delete(0, 'end')
            ln.delete(0, 'end')
            cn.delete(0, 'end')
            ei.delete(0, 'end')
            pa.delete(0, 'end')
            cp.delete(0, 'end')
            fn.focus_set()
         except EXCEPTION as e:
            print(e)
            db.rollback()
            db.close()

rt=Tk()
width= rt.winfo_screenwidth()
height= rt.winfo_screenheight()
rt.title("Registration Page")
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
t=Label(frame2,text="Register Here",font="Constantia 15 bold",fg="red",bg="cyan")
t.place(x=325,y=10)
frame3=Frame(frame1,bg="#f6ebeb")
frame3.place(x=20,y=110,width=790,height=400)
t1=Label(frame3,text="First Name:",font="Constantia 15 bold",bg="#f6ebeb")
t1.place(x=50,y=10)
fn=ttk.Entry(frame3,font="Constantia 15 bold")
fn.place(x=50,y=40,width=250)
t2=Label(frame3,text="Last Name:",font="Constantia 15 bold",bg="#f6ebeb")
t2.place(x=480,y=10)
ln=ttk.Entry(frame3,font="Constantia 15 bold")
ln.place(x=480,y=40,width=250)
t3=Label(frame3,text="Contact No:",font="Constantia 15 bold",bg="#f6ebeb")
t3.place(x=50,y=80)
cn=ttk.Entry(frame3,font="Constantia 15 bold")
cn.place(x=50,y=110,width=250)
t4=Label(frame3,text="Email ID:",font="Constantia 15 bold",bg="#f6ebeb")
t4.place(x=480,y=80)
ei=ttk.Entry(frame3,font="Constantia 15 bold")
ei.place(x=480,y=110,width=250)
t5=Label(frame3,text="Date Of Birth:",font="Constantia 15 bold",bg="#f6ebeb")
t5.place(x=50,y=150)
cal=DateEntry(frame3,font="Constantia 15 bold",bg="gray",fg="white")
cal.place(x=50,y=180,width=250)
t6=Label(frame3,text="Password:",font="Constantia 15 bold",bg="#f6ebeb")
t6.place(x=480,y=150)
pa=ttk.Entry(frame3,font="Constantia 15 bold")
pa.place(x=480,y=180,width=250)
pa.config(show="*")
t7=Label(frame3,text="Confirm Password:",font="Constantia 15 bold",bg="#f6ebeb")
t7.place(x=260,y=220)
cp=ttk.Entry(frame3,font="Constantia 15 bold")
cp.place(x=260,y=250,width=250)
cp.config(show="*")
vag=IntVar()
chk=Checkbutton(frame3,variable=vag,text="I Agree the Terms and Conditions",font="Constantia 15 bold",bg="#f6ebeb",onvalue=1,offvalue=0)
chk.place(x=200,y=290)
b_1 = Button(frame3, text="Register",font="Constantia 10 bold", width='15', height='1', command=reg )
b_1.place(x=200,y=360)
b_2 = Button(frame3, text="Back",font="Constantia 10 bold", width='15', height='1',command=b )
b_2.place(x=420,y=360)
rt.mainloop()