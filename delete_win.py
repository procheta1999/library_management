from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
d=['Select']

def h():
    rt.destroy()
    import bd_win

def info():
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    mycursor.execute("select id from books_details")
    rows = mycursor.fetchall()
    for row in rows:
        (row1)=row
        print(str(row1[0]))
        d.append(row1[0])
    print(d)
    db.commit()
    db.close()
def getdata(event):
    pass
    # currow = medtab.focus()
    # contents = medtab.item(currow)
    # row = contents['values']
    # bn.delete(0, END)
    # # bi.delete(0, END)
    # a.delete(0, END)
    # g.delete(0, END)
    # n.delete(0, END)
    # bn.insert(0, row[0])
    # # bi.insert(0, row[1])
    # a.insert(0, row[2])
    # g.insert(0, row[3])
    # n.insert(0, row[4])


def fetchdata():
    # bn1 = bn.get()
    # bi1 = bi.get()
    # a1 = a.get()
    # g1 = g.get()
    # n1 = n.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    mycursor.execute("select * from books_details")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        medtab.delete(*medtab.get_children())
    for row in rows:
        medtab.insert('', END, values=row)
    db.commit()
    db.close()


def add():
    if bn.get() == "" or bi.get() == "" or a.get() == "" or g.get() == "" or n.get() == "":
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
            sql = "insert into books_details(book_name,id,author,genre,sample_no)values(%s,%s,%s,%s,%s)"
            val = (bn2, bi2, a2, g2, n2)
            mycursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("information", "Record Inserted successfully")
            # fectdata()
            cleardata()
        except EXCEPTION as e:
            print(e)
            db.rollback()
            db.close()


def update():
    bn3 = bn.get()
    a3 = a.get()
    g3 = g.get()
    n3 = n.get()
    if bn3=='Select':
        messagebox.showinfo("error", "Choose Book ID")
    else:
        db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
        mycursor = db.cursor()
        try:
            sql = "update books_details set author=%s,genre=%s,sample_no=%s where id=%s"
            val = (a3,g3,n3,bn3)
            mycursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("information", "Record Updated successfully")
            bn.delete(0, END)
            a.delete(0, END)
            g.delete(0, END)
            n.delete(0, END)
            fetchdata()
        except EXCEPTION as e:
            print(e)
            db.rollback()
            db.close()


def delete():
    bi4 = bn.get()
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    if bi4=="Select":
        messagebox.showinfo("error", "Choose Book ID")
    else:
        try:
            sql = "delete from books_details where id=%s"
            val = (bi4,)
            mycursor.execute(sql, val)
            db.commit()
            messagebox.showinfo("information", "Record Deleted successfully")
            bn.delete(0, END)
            fetchdata()
            cleardata()
        except EXCEPTION as e:
            print(e)
            db.rollback()
            db.close()


def cleardata():
    bn.delete(0, 'end')
    bi.delete(0, 'end')
    a.delete(0, 'end')
    g.delete(0, 'end')
    n.delete(0, 'end')
    bn.focus_set()


def fetchdata1():
    ser1 = comboser.get()

    lsearch1 = str(lsearch.get())+"%"
    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    print(lsearch1)
    try:
        if ser1 == 'Book ID':
            sql = "select * from books_details where id like %s"
        elif ser1 == 'Author':
            sql = "select * from books_details where author like %s"
        elif ser1 == 'Genre':
            sql = "select * from books_details where genre like %s"
        else:
            messagebox.showinfo("error", "Choose a field from dropdown")
            sql = "select * from books_details"
        val = (lsearch1,)
        print(lsearch1,sql)
        mycursor.execute(sql, val)
        rows = mycursor.fetchall()
        print(rows)
        if len(rows) != 0:
            medtab.delete(*medtab.get_children())
        else:
            messagebox.showinfo("error", "No Data Found")
        for row in rows:
            medtab.insert('', END, values=row)
        db.commit()
        db.close()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()

info()
rt = Tk()
width= rt.winfo_screenwidth()
height= rt.winfo_screenheight()
rt.title("Delete Book Information")
rt.geometry("%dx%d" % (width, height))
bg = ImageTk.PhotoImage(file="pic3.jpg", master=rt)
bglb = Label(rt, image=bg)
bglb.place(x=0, y=0, relwidth=1, relheight=1)
frame1 = Frame(rt, bg="white")
frame1.place(x=10, y=10, width=1230, height=530)
frame2 = Frame(frame1, bg="cyan")
frame2.place(x=20, y=20, width=1190, height=70)
t = Label(frame2, text="Delete Book Information", font="Constantia 15 bold", fg="red", bg="cyan")
t.place(x=565, y=10)
ta = Button(frame2, text="Back", font="Constantia 10 bold", width='15', height='1', command=h)
ta.place(x=1045, y=10)
frame3 = Frame(frame1, bg="#f6ebeb")
frame3.place(x=20, y=80, width=430, height=435)
t1 = Label(frame3, text="Delete", font="Constantia 15 bold underline", bg="#f6ebeb")
t1.grid(row=0, columnspan=2, pady=15)
t2 = Label(frame3, text="Book ID:", font="Constantia 15 bold", bg="#f6ebeb")
t2.grid(row=1, column=0, pady=15, padx=10, sticky="w")
bn = ttk.Combobox(frame3, font="Constantia 15 bold", state="readonly")
bn['values']=tuple(d)
bn.current(0)
bn.grid(row=1, column=1, pady=5, padx=5, sticky="w")
# t3 = Label(frame3, text="Book ID:", font="Constantia 15 bold", bg="#f6ebeb")
# t3.grid(row=2, column=0, pady=15, padx=10, sticky="w")
# bi = Entry(frame3, font="Constantia 15 bold")
# bi.grid(row=2, column=1, pady=15, padx=10, sticky="w")
# t4 = Label(frame3, text="Author:", font="Constantia 15 bold", bg="#f6ebeb")
# t4.grid(row=3, column=0, pady=15, padx=10, sticky="w")
# a = Entry(frame3, font="Constantia 15 bold")
# a.grid(row=3, column=1, pady=15, padx=10, sticky="w")
# t5 = Label(frame3, text="Genre:", font="Constantia 15 bold", bg="#f6ebeb")
# t5.grid(row=4, column=0, pady=15, padx=10, sticky="w")
# g = Entry(frame3, font="Constantia 15 bold")
# g.grid(row=4, column=1, pady=15, padx=10, sticky="w")
# t6 = Label(frame3, text="No. of copies:", font="Constantia 15 bold", bg="#f6ebeb")
# t6.grid(row=5, column=0, pady=15, padx=10, sticky="w")
# n = Entry(frame3, font="Constantia 15 bold")
# n.grid(row=5, column=1, pady=15, padx=10, sticky="w")
frame4 = Frame(frame3, bg="#f6ebeb")
frame4.place(x=130, y=150, width=390, height=50)
addbt = Button(frame4, text="Delete", width=10, command=delete).grid(row=0, column=1, padx=10, pady=10)
# updatebt = Button(frame4, text="Update", width=10, command=update).grid(row=0, column=1, padx=10, pady=10)

# clrt = Button(frame4, text="Clear", width=10, command=cleardata).grid(row=0, column=2, padx=10, pady=10)
# frame6 = Frame(frame1, bg="#f6ebeb")
# frame6.place(x=20, y=530, width=420, height=150)
# t9 = Label(frame6, text="Update or Delete Books", font="Constantia 15 bold underline", bg="#f6ebeb")
# t9.grid(row=0, column=1, columnspan=30, padx=90, pady=10)
# updatebt = Button(frame6, text="Update", width=10, command=update).grid(row=2, column=1, padx=70, pady=40)
# detebt = Button(frame6, text="Delete", width=10, command=delete).grid(row=2, column=2, padx=10, pady=20)
frame5 = Frame(frame1, bg="#f6ebeb")
frame5.place(x=450, y=80, width=760, height=435)
# t7 = Label(frame5, text="Search By", font="Constantia 15 bold", bg="#f6ebeb")
# t7.grid(row=0, column=0, pady=10, padx=10, sticky="w")
# comboser = ttk.Combobox(frame5, width=10, font="Constantia 15 bold", state='readonly')
# comboser['values'] = ("Select", "Book ID", "Author", "Genre")
# comboser.current(0)
# comboser.grid(row=0, column=1, padx=10, pady=10)
# lsearch = Entry(frame5, font="Constantia 15 bold")
# lsearch.grid(row=0, column=2, pady=10, padx=10, sticky="w")
# serbt = Button(frame5, text="Search", width=10, command=fetchdata1).grid(row=0, column=3, padx=10, pady=10)
# showbt = Button(frame5, text="Show All", width=10, command=fetchdata).grid(row=0, column=4, padx=10, pady=10)
tabfrm = Frame(frame5, bg="#f6ebeb")
tabfrm.place(x=10, y=50, width=740, height=370)
scrollx = Scrollbar(tabfrm, orient=HORIZONTAL)
scrolly = Scrollbar(tabfrm, orient=VERTICAL)
medtab = ttk.Treeview(tabfrm, columns=("a", "b", "c", "d", "e"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("a", text="Book ID")
medtab.heading("b", text="Book Name")
medtab.heading("c", text="No. of Copies")
medtab.heading("d", text="Author")
medtab.heading("e", text="Genre")
medtab['show'] = "headings"
medtab.column("a", width=100)
medtab.column("b", width=100)
medtab.column("c", width=100)
medtab.column("d", width=100)
medtab.column("e", width=100)
medtab.pack(fill=BOTH, expand=1)
medtab.bind("<ButtonRelease-1>", getdata)
fetchdata()
# b_1 = Button(rt, text="Back",font="Constantia 10 bold", width='15', height='1',command=h )
# b_1.place(x=555,y=250)
rt.mainloop()
