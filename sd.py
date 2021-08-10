from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import date
from datetime import timedelta
from datetime import datetime
sname=''
sid=''
isdate=''
rtdate=''
no=''
def h():
    rt.destroy()
    import mn_win


def c():
    global sname,sid,isdate,rtdate,no
    sname = bn.get()
    sid = bi.get()
    isdate = a.get()
    rtdate = g.get()
    no = n.get()
    # print(sname, sid, isdate, rtdate, no)
    rt.destroy()
    import fine_win
    """a=bi.get()
    global fi,daysno
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    try:
        sql1="select ry,rm,rd from students_details where student_id=a"
        sql7="select bno from students_details where student_id=a"
        mycursor.execute(sql1)
        date = mycursor.fetchall()
        datey=date[0]
        datem=date[1]
        dated=date[2]
        date1=date(datey,datem,dated)
        date2 = date.today()
        mycursor.execute(sql7)
        bn = mycursor.fetchall()
        if (date1 <= date2):
            fi = 0
        else:
            daysno = (date2 - date1).days
            fi = 2 * daysno * bn
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()"""



def getdata(event):
    currow = medtab.focus()
    contents = medtab.item(currow)
    row = contents['values']
    bn.delete(0, END)
    bi.delete(0, END)
    a.delete(0, END)
    g.delete(0, END)
    n.delete(0, END)
    bn.insert(0, row[0])
    bi.insert(0, row[1])
    a.insert(0, row[2])
    g.insert(0, row[3])
    n.insert(0, row[4])


def fetchdata():
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    mycursor.execute("select * from students_details")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        medtab.delete(*medtab.get_children())
    for row in rows:
        medtab.insert('', END, values=row)
    db.commit()
    db.close()


def add():
    pass
    """if bn.get() == "" or bi.get() == "" or a.get() == "" or g.get() == "" or n.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        bn2 = bn.get()
        bi2 = bi.get()
        a2 = a.get()
        g2 = g.get()
        n2 = n.get()
        db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
        mycursor = db.cursor()
        try:
            sql = "insert into students_details(student_name,student_id,idate,rdate,bno)values(%s,%s,%s,%s,%s)"
            val = (bn2,bi2,a2,g2,n2)
            mycursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("information", "Record Inserted successfully")
            fectdata()
            cleardata()
        except EXCEPTION as e:
            print(e)
            db.rollback()
            db.close()"""


def re():
    today = date.today()
    global nd
    bi3 = bi.get()
    nd = today + timedelta(days=30)
    ndy = int(nd.strftime("%Y"))
    ndm = int(nd.strftime("%m"))
    ndd = int(nd.strftime("%d"))
    nd = str(nd)
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    try:
        sql = "update students_details set idate=%s,rdate=%s,ry=%s,rm=%s,rd=%s where student_id=%s"
        val = (today, nd, ndy, ndm, ndd, bi3,)
        mycursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("information", "Record Updated successfully")
        bn.delete(0, END)
        bi.delete(0, END)
        a.delete(0, END)
        g.delete(0, END)
        n.delete(0, END)
        fetchdata()
        cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()


def delete():
    pass
    """bi4 = bi.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    try:
        sql = "delete from students_details where bno=%s"
        val = (bi4,)
        mycursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("information", "Record Deleted successfully")
        bn.delete(0, END)
        bi.delete(0, END)
        a.delete(0, END)
        g.delete(0, END)
        n.delete(0, END)
        fetchdata()
        cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()"""


def cleardata():
    bn.delete(0, 'end')
    bi.delete(0, 'end')
    a.delete(0, 'end')
    g.delete(0, 'end')
    n.delete(0, 'end')
    bn.focus_set()


def fetchdata1():
    pass
    """ser1 = comboser.get()
    lsearch1 = lsearch.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    mycursor.execute("select * from students_details where " + str(ser1) + " LIKE '%" + str(lsearch1) + "%'")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        medtab.delete(*medtab.get_children())
    for row in rows:
        medtab.insert('', END, values=row)
    db.commit()
    db.close()"""


rt = Tk()
width = rt.winfo_screenwidth()
height = rt.winfo_screenheight()
rt.title("Students Database")
rt.geometry("%dx%d" % (width, height))
rt.iconbitmap("images/open-book.ico")
bg = ImageTk.PhotoImage(file="images/pic3.jpg", master=rt)
bglb = Label(rt, image=bg)
bglb.place(x=0, y=0, relwidth=1, relheight=1)
frame1 = Frame(rt, bg="white")
frame1.place(x=180, y=100, width=1230, height=530)
frame2 = Frame(frame1, bg="cyan")
frame2.place(x=20, y=20, width=1190, height=50)
t = Label(frame2, text="Students Database", font="Constantia 15 bold", fg="red", bg="cyan")
t.place(x=565, y=10)
ta = Button(frame2, text="Back", font="Constantia 10 bold", width='15', height='1', command=h)
ta.place(x=1045, y=10)
frame3 = Frame(frame1, bg="#f6ebeb")
frame3.place(x=20, y=80, width=420, height=435)
t1 = Label(frame3, text="Manage Students", font="Constantia 15 bold underline", bg="#f6ebeb")
t1.grid(row=0, columnspan=2, pady=5)
t2 = Label(frame3, text="Student Name:", font="Constantia 15 bold", bg="#f6ebeb")
t2.grid(row=1, column=0, pady=5, padx=5, sticky="w")
bn = Entry(frame3, font="Constantia 15 bold")
bn.grid(row=1, column=1, pady=5, padx=5, sticky="w")

t3 = Label(frame3, text="Student ID:", font="Constantia 15 bold", bg="#f6ebeb")
t3.grid(row=2, column=0, pady=5, padx=5, sticky="w")
bi = Entry(frame3, font="Constantia 15 bold")
bi.grid(row=2, column=1, pady=5, padx=5, sticky="w")
t4 = Label(frame3, text="Issue Date:", font="Constantia 15 bold", bg="#f6ebeb")
t4.grid(row=3, column=0, pady=5, padx=5, sticky="w")
a = Entry(frame3, font="Constantia 15 bold")
a.grid(row=3, column=1, pady=5, padx=5, sticky="w")
t5 = Label(frame3, text="Return Date:", font="Constantia 15 bold", bg="#f6ebeb")
t5.grid(row=4, column=0, pady=5, padx=5, sticky="w")
g = Entry(frame3, font="Constantia 15 bold")
g.grid(row=4, column=1, pady=5, padx=5, sticky="w")
t6 = Label(frame3, text="No. of books:", font="Constantia 15 bold", bg="#f6ebeb")
t6.grid(row=5, column=0, pady=5, padx=5, sticky="w")
n = Entry(frame3, font="Constantia 15 bold")
n.grid(row=5, column=1, pady=5, padx=5, sticky="w")

# t7=Label(frame3,text="Actual Date:",font="Constantia 15 bold",bg="#f6ebeb")
# t7.grid(row=6,column=0,pady=5,padx=5,sticky="w")
# t8=Label(frame3,text=str(date.today()),font="Constantia 15 bold",bg="white").grid(row=6,column=1,pady=5,padx=5,sticky="w")
# t9=Label(frame3,text=str(date.today()),font="Constantia 15 bold",bg="white").grid(row=7,column=0,pady=5,padx=5,sticky="w")
# t9=Label(frame3,text="Fine Amt:",font="Constantia 15 bold",bg="#f6ebeb")
# t9.grid(row=7,column=0,pady=5,padx=5,sticky="w")
# t10=Label(frame3,text=str(fi),font="Constantia 15 bold",bg="white").grid(row=7,column=1,pady=5,padx=5,sticky="w")
frame4 = Frame(frame3, bg="#f6ebeb")
frame4.place(x=8, y=370, width=390, height=50)
# addbt=Button(frame4,text="Add",width=10,command=add).grid(row=0,column=0,padx=10,pady=10)
updatebt = Button(frame4, text="Return", width=10, command=c).place(x=30, y=13)
updatebt1 = Button(frame4, text="Reissue", width=10, command=re).place(x=155, y=13)
detebt = Button(frame4, text="Clear", width=10, command=cleardata).place(x=280, y=13)
# clrt=Button(frame4,text="Clear",width=10,command=cleardata).grid(row=0,column=3,padx=10,pady=10)
frame5 = Frame(frame1, bg="#f6ebeb")
frame5.place(x=450, y=80, width=760, height=435)
# t7=Label(frame5,text="Search By",font="Constantia 15 bold",bg="#f6ebeb")
# t7.grid(row=0,column=0,pady=10,padx=10,sticky="w")
# comboser=ttk.Combobox(frame5,width=10,font="Constantia 15 bold",state='readonly')
# comboser['values']=("Select","Book ID","Author","Genre")
# comboser.current(0)
# comboser.grid(row=0,column=1,padx=10,pady=10)
# lsearch=Entry(frame5,font="Constantia 15 bold")
# lsearch.grid(row=0,column=2,pady=10,padx=10,sticky="w")
# serbt=Button(frame5,text="Search",width=10,command=fetchdata1).grid(row=0,column=3,padx=10,pady=10)
# showbt=Button(frame5,text="Show All",width=10,command=fetchdata).grid(row=0,column=4,padx=10,pady=10)
tabfrm = Frame(frame5, bg="#f6ebeb")
tabfrm.place(x=10, y=50, width=740, height=375)
scrollx = Scrollbar(tabfrm, orient=HORIZONTAL)
scrolly = Scrollbar(tabfrm, orient=VERTICAL)
medtab = ttk.Treeview(tabfrm, columns=("a", "b", "c", "d", "e"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("a", text="Student Name")
medtab.heading("b", text="Student ID")
medtab.heading("c", text="Issue Date")
medtab.heading("d", text="Return Date")
medtab.heading("e", text="No. of books")
medtab['show'] = "headings"
medtab.column("a", width=100)
medtab.column("b", width=100)
medtab.column("c", width=100)
medtab.column("d", width=100)
medtab.column("e", width=100)
medtab.pack(fill=BOTH, expand=1)
medtab.bind("<ButtonRelease-1>", getdata)
fetchdata()

rt.mainloop()


# def sname():
#     return bn.get()
