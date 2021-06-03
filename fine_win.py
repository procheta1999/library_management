from tkinter import *
from tkinter import ttk, messagebox
from datetime import date
import mysql.connector
from sd import sname,sid,isdate,rtdate,no

# import sd_win
def delay():
    rt.destroy()
    import sd
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y


# To store number of days in all months from
# January to Dec.
monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]


# This function counts number of leap years
# before the given date


def countLeapYears(d):
    years = d.y

    # Check if the current year needs to be considered
    # for the count of leap years or not
    if (d.m <= 2):
        years -= 1

    # An year is a leap year if it is a multiple of 4,
    # multiple of 400 and not a multiple of 100.
    return int(years / 4) - int(years / 100) + int(years / 400)


# This function returns number of days between two
# given dates
def getDifference(dt1, dt2):
    # COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1'

    # initialize count using years and day
    n1 = dt1.y * 365 + dt1.d

    # Add days for months in given date
    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]

    # Since every leap year is of 366 days,
    # Add a day for every leap year
    n1 += countLeapYears(dt1)

    # SIMILARLY, COUNT TOTAL NUMBER OF DAYS BEFORE 'dt2'

    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)

    # return difference between two counts
    return (n2 - n1)
def pay():

    db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
    mycursor = db.cursor()
    try:
        sql = "delete from students_details where student_id=%s"
        val = (sid,)
        mycursor.execute(sql, val)
        messagebox.showinfo("information", "Record Deleted successfully")
        delay()
        db.commit()


        # bn.delete(0, END)
        # bi.delete(0, END)
        # a.delete(0, END)
        # g.delete(0, END)
        # n.delete(0, END)
        # fetchdata()
        # cleardata()
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()


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
t5 = Label(rt, text="Today's Date:", font="Constantia 15 bold", bg="white")
t5.place(x=90, y=210)
t6 = Label(rt, text="No. of books issued:", font="Constantia 15 bold", bg="white")
t6.place(x=90, y=250)
t7 = Label(rt, text="Fine Amt:", font="Constantia 15 bold", bg="white")
t7.place(x=90, y=290)
b_1 = Button(rt, text="Paid", font="Constantia 10 bold", width='15', height='1', command=pay)
b_1.place(x=220, y=360)
# b_2 = Button(rt, text="Students Database",font="Constantia 10 bold", width='15', height='1', command=)
# b_2.place(x=190,y=250)

fi=0
date3=[]
b = sname
a = sid
c = isdate
d = rtdate
e = no
print('b',b)
db = mysql.connector.connect(host="localhost", user="root", password="", database="books")
mycursor = db.cursor()
try:
    sql1 = "select ry,rm,rd from students_details where student_id=%s"
    sql7 = "select bno from students_details where student_id=%s"
    val = (a,)
    mycursor.execute(sql1, val)
    date1 = mycursor.fetchall()
    date1=list(date1[0])
    date1=date1[::-1]
    date1=tuple(date1)
    date2 = date.today()
    date2=str(date2).split('-')
    for i in range(0,len(date2)):
        date3.append(int(date2[i]))
    date3=date3[::-1]
    date3=tuple(date3)
    mycursor.execute(sql7, val)
    bn = mycursor.fetchall()
    print('date1', date1,date3)
    dt1=Date(date1[0],date1[1],date1[2])
    dt2=Date(date3[0],date3[1],date3[2])
    print(getDifference(dt1, dt2), "days")
    if getDifference(dt1,dt2)<=0:
        fi=0
    else:
        fi=int(getDifference(dt1,dt2))*int(e)
    # if date1[0]==date3[0]:
    #     if date1[1]>=date3[1]:
    #         if date1[2]>=date3[2]:
    #             fi=0
            # else:
            #     daysno=date3[2]-date1[2]
            #     fi=2*daysno*e
    # if date1 <= date3:
    #     fi = 0
    # else:
    #     daysno = (date3 - date1).days
    #     fi = 2 * daysno * bn
except EXCEPTION as e:
    print(e)
    db.rollback()
    db.close()

t8 = Label(rt, text=str(b), font="Constantia 15 bold", bg="white").place(x=320, y=50)
t9 = Label(rt, text=str(a), font="Constantia 15 bold", bg="white").place(x=320, y=90)
t10 = Label(rt, text=str(c), font="Constantia 15 bold", bg="white").place(x=320, y=130)
t11 = Label(rt, text=str(d), font="Constantia 15 bold", bg="white").place(x=320, y=170)
t12 = Label(rt, text=str(date.today()), font="Constantia 15 bold", bg="white").place(x=320, y=210)
t13 = Label(rt, text=str(e), font="Constantia 15 bold", bg="white").place(x=320, y=250)
t14 = Label(rt, text=str(fi), font="Constantia 15 bold", bg="white").place(x=320, y=290)

rt.mainloop()
