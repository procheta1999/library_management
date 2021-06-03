from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


def bd():
    rt.destroy()
    import bd_win


def sd():
    rt.destroy()
    import sd


def lg():
    rt.destroy()
    import Project1


rt = Tk()
width= rt.winfo_screenwidth()
height= rt.winfo_screenheight()
rt.title("Menu")
rt.geometry("%dx%d" % (width, height))
bg = ImageTk.PhotoImage(file="pic3.jpg", master=rt)
bglb = Label(rt, image=bg)
bglb.place(x=0, y=0, relwidth=1, relheight=1)
t = Label(rt, text="Library Management System", font="Constantia 15 bold", bg="cyan", fg="red", padx=25, pady=5)
t.place(x=600, y=200)
b_1 = Button(rt, text="Books Database", font="Constantia 10 bold", width='15', height='1', command=bd)
b_1.place(x=670, y=350)
b_2 = Button(rt, text="Students Database", font="Constantia 10 bold", width='15', height='1', command=sd)
b_2.place(x=670, y=400)
b_3 = Button(rt, text="Logout", font="Constantia 10 bold", width='15', height='1', command=lg)
b_3.place(x=670, y=450)
rt.mainloop()
