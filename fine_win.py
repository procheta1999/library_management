from tkinter import *
from tkinter import ttk
from datetime import date


# import sd_win


def pay():
    rt.destroy()
    import sd_win
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


rt = Tk()
rt.title("Fine Collection")
rt.geometry("550x450")
rt.configure(bg='#f6ebeb')
t1 = Label(rt, text="Details:", font="Constantia 15 bold underline", bg="#f6ebeb")
t1.place(x=240, y=10)
t1 = Label(rt, text="Student Name:", font="Constantia 15 bold", bg="white")
t1.place(x=90, y=50)
t2 = Label(rt, text="Student ID:", font="Constantia 15 bold", bg="white")
t2.place(x=90, y=90)
t3 = Label(rt, text="Issue Date:", font="Constantia 15 bold", bg="white")
t3.place(x=90, y=130)
t4 = Label(rt, text="Return Date:", font="Constantia 15 bold", bg="white")
t4.place(x=90, y=170)
t5 = Label(rt, text="Actual Date of return:", font="Constantia 15 bold", bg="white")
t5.place(x=90, y=210)
t6 = Label(rt, text="No. of books issued:", font="Constantia 15 bold", bg="white")
t6.place(x=90, y=250)
t7 = Label(rt, text="Fine Amt:", font="Constantia 15 bold", bg="white")
t7.place(x=90, y=290)
b_1 = Button(rt, text="Paid", font="Constantia 10 bold", width='15', height='1', command=pay)
b_1.place(x=220, y=360)
# b_2 = Button(rt, text="Students Database",font="Constantia 10 bold", width='15', height='1', command=)
# b_2.place(x=190,y=250)
"""
global fi;
import sd_win
b=sd_win.bn.get()
a=sd_win.bi.get()
c=sd_win.a.get()
d=sd_win.g.get()
e=sd_win.n.get()
db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
mycursor = db.cursor()
try:
    sql1="select ry,rm,rd from students_details where student_id=a"
    sql7="select bno from students_details where student_id=a"
    mycursor.execute(sql1)
        date1 = mycursor.fetchall()
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
    db.close()
"""
# t8=Label(rt,text=str(b),font="Constantia 15 bold",bg="white").place(x=320,y=50)
# t9=Label(rt,text=str(a),font="Constantia 15 bold",bg="white").place(x=320,y=90)
# t10=Label(rt,text=str(c),font="Constantia 15 bold",bg="white").place(x=320,y=130)
# t11=Label(rt,text=str(d),font="Constantia 15 bold",bg="white").place(x=320,y=170)
t12 = Label(rt, text=str(date.today()), font="Constantia 15 bold", bg="white").place(x=370, y=210)
# t13=Label(rt,text=str(e),font="Constantia 15 bold",bg="white").place(x=320,y=250)
# t14=Label(rt,text=str(fi),font="Constantia 15 bold",bg="white").place(x=320,y=290)


rt.mainloop()
