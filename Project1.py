from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


def sd():
    rt.destroy()
    import sd_win


def rg():
    rt.destroy()
    import rg_win


rt = Tk()
width= rt.winfo_screenwidth()
height= rt.winfo_screenheight()
print(width,height)
rt.title("Home Page")
rt.geometry("%dx%d" % (width, height))
# rt.maxsize(1250,550)
# rt.minsize(1250,550)
bg = ImageTk.PhotoImage(file="pic3.jpg",master=rt)
bglb = Label(rt, image=bg)
bglb.place(x=0, y=0, relwidth=1, relheight=1)
t = Label(rt, text="Library Management System", font="Constantia 15 bold", bg="cyan", fg="red", padx=25, pady=5)
t.place(x=600, y=200)
b_2 = Button(rt, text="Login", font="Constantia 10 bold", width='15', height='1', command=sd)
b_2.place(x=670, y=350)
b_3 = Button(rt, text="Register Now", font="Constantia 10 bold", width='15', height='1', command=rg)
b_3.place(x=670, y=400)
rt.mainloop()
