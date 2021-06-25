from tkinter import *
from PIL import ImageTk, Image  # PIL -> Pillow
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime

mypass = "root"
mydatabase="LMS_db"

def connectdb():
    global con, cur, enter
    # Enter your username and password of MySQL
    con = p.connect(host="127.0.0.1", user="root", passwd="root")
    cur = con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS Library')
    cur.execute('USE Library')
    enter=1

    if enter == 1:
        l = 'CREATE TABLE IF NOT EXISTS Login(name varchar(20) NOT NULL,userid varchar(10) PRIMARY KEY,branch varchar(20),mobile int(10) UNIQUE);'
        b = 'CREATE TABLE IF NOT EXISTS Books(ISBN_NO int Primary key,Book_Name varchar(100) NOT NULL,Author varchar(30) NOT NULL, Language varchar(100) NOT NULL,Book_id varchar(8) NOT NULL, Publication varchar(50) Not Null,Publication_year int, No_Of_Copies int,Copies_Available int, Shelf_No int);'
        i = 'CREATE TABLE IF NOT EXISTS BookIssue(stdid varchar(20) UNIQUE NOT NULL,Book_id varchar(10) NOT NULL, Book_Name varchar(50) NOT NULL,issue date,exp date)'
        cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        enter = enter + 1
    query = 'SELECT * FROM Login'
    cur.execute(query)
    pass


month=['January','February','March','April','May','June','July','August','September','October','November','December']
y = list(range(2015, 2040))
d = list(range(1,32))




root = Tk()
root.title("My Library")
root.minsize(width=400, height=400)
root.geometry("600x500")

same = True
n = 0.25




headingFrame1 = Frame(root, bg="#91e890", bd=6)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n CodeKul Library", bg='#e8b590', fg='white', font=('Courier', 18))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


def addbooks():
    connectdb()
    q = 'INSERT INTO Books VALUE("%i","%s","%s","%s","%s","%s","%i","%i","%i","%i")'
    global cur, con
    cur.execute(q % (int(e1.get()), e2.get(), e3.get(), e5.get(), e4.get(), e6.get(), int(e7.get()), int(e8.get()), int(e9.get()), int(e10.get())))
    con.commit()
    root.destroy()
    messagebox.showinfo("Book", "Book Added")
    closedb()
   # libr()
    pass


def closebooks():
    global root
    root.destroy()
   # libr()

    pass


def addbook():
    global root
    root.destroy()
    root = Tk()
    root.title('Add Book')
    root.geometry("400x600+480+180")
    root.resizable(False, False)
    isbn = Label(root, text='ISBN No.')
    tit = Label(root, text='TITLE')
    auth = Label(root, text='AUTHOR')
    lang = Label(root, text='Language')
    ser = Label(root, text='BOOK ID')
    pub = Label(root, text='Publication')
    pub_yr = Label(root, text='Publication Year')
    cop = Label(root, text='Copies Added')
    ava = Label(root, text='Available Copies')
    shelf_no = Label(root, text='Shelf No.')
    global e1, b, b1
    e1 = Entry(root, width=25)
    global e2
    e2 = Entry(root, width=25)
    global e3
    e3 = Entry(root, width=25)
    global e4
    e4 = Entry(root, width=25)
    global e5
    e5 = Entry(root, width=25)
    global e6
    e6 = Entry(root, width=25)
    global e7
    e7 = Entry(root, width=25)
    global e8
    e8 = Entry(root, width=25)
    global e9
    e9 = Entry(root, width=25)
    global e10
    e10 = Entry(root, width=25)
    b = Button(root, height=2, width=21, text=' ADD BOOK ', command=addbooks)
    b1 = Button(root, height=2, width=21, text=' CLOSE ', command=closebooks)
    isbn.place(x=70, y=50)
    tit.place(x=70, y=90)
    auth.place(x=70, y=130)
    ser.place(x=70, y=170)
    lang.place(x=70, y=210)
    pub.place(x=70, y=250)
    pub_yr.place(x=70, y=290)
    cop.place(x=70, y=330)
    ava.place(x=70, y=370)
    shelf_no.place(x=70, y=410)
    e1.place(x=180, y=50)
    e2.place(x=180, y=90)
    e3.place(x=180, y=130)
    e4.place(x=180, y=170)
    e5.place(x=180, y=210)
    e6.place(x=180, y=250)
    e7.place(x=180, y=290)
    e8.place(x=180, y=330)
    e9.place(x=180, y=370)
    e10.place(x=180, y=410)
    b.place(x=180, y=450)
    b1.place(x=180, y=492)
    root.mainloop()
    pass

def deletebooks():
    connectdb()
    if e2.get() == 'Library@7':
        q = 'DELETE FROM Books WHERE Book_id="%i"'
        cur.execute(q % (int(e1.get())))
        con.commit()
        root.destroy()
        messagebox.showinfo("Delete", "Book Deleted")
        closedb()
       # libr()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        closedb()
    pass


def deletebook():
    global root
    root.destroy()
    root = Tk()
    root.title('Delete Book')
    root.geometry("400x400+480+180")
    root.resizable(False, False)
    usid = Label(root, text='BOOK ID')
    paswrd = Label(root, text='PASSWORD')
    global e1
    e1 = Entry(root)
    global e2, b2
    e2 = Entry(root)
    b1 = Button(root, height=2, width=17, text=' DELETE ', command=deletebooks)
    b2 = Button(root, height=2, width=17, text=' CLOSE ', command=closebooks)
    usid.place(x=80, y=100)
    paswrd.place(x=70, y=140)

    e1.place(x=180, y=100)
    e2.place(x=180, y=142)
    b1.place(x=180, y=180)
    b2.place(x=180, y=230)
    root.mainloop()
    pass


def viewbook():
    root = Tk()
    root.title('View Books')
    root.geometry("1000x300+10+20")
    root.resizable(True, True)

    treeview = Treeview(root, columns=("ISBN_No", "Book_Name", "Author", "Book_id", "Language","Publication", "Publication_Year", "No_of_Copies", "Copies_Available", "Shelf_No"), show='headings')
    treeview.heading("ISBN_No", text="ISBN No")
    treeview.heading("Book_Name", text="Book Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Book_id", text="Book Id")
    treeview.heading("Language", text="Language")
    treeview.heading("Publication", text="Publication")
    treeview.heading("Publication_Year", text="Publication Year")
    treeview.heading("No_of_Copies", text="Copies Added")
    treeview.heading("Copies_Available", text="Copies Available")
    treeview.heading("Shelf_No", text="Shelf No")
    treeview.column("ISBN_No", anchor='center')
    treeview.column("Book_Name", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Book_id", anchor='center')
    treeview.column("Language", anchor='center')
    treeview.column("Publication", anchor='center')
    treeview.column("Publication_Year", anchor='center')
    treeview.column("No_of_Copies", anchor='center')
    treeview.column("Copies_Available", anchor='center')
    treeview.column("Shelf_No", anchor='center')
    index = 0
    iid = 0
    connectdb()
    q = 'SELECT * FROM Books'
    cur.execute(q)
    details = cur.fetchall()
    for row in details:
        treeview.insert("", index, iid, value=row)
        index = iid = index + 1
    treeview.pack()
    root.mainloop()
    closedb()
    pass


def issuebooks():
    connectdb()
    q = 'INSERT INTO BookIssue VALUE("%s","%s","%s","%s")'
    i = datetime.datetime(int(com1y.get()), month.index(com1m.get()) + 1, int(com1d.get()))
    e = datetime.datetime(int(com2y.get()), month.index(com2m.get()) + 1, int(com2d.get()))
    i = i.isoformat()
    e = e.isoformat()
    cur.execute(q % (e1.get(), e4.get(), i, e))
    con.commit()
    root.destroy()
    messagebox.showinfo("Book", "Book Issued")
    closedb()
   # libr()
    pass


def issuebook():
    global root
   # root.destroy()
    root = Tk()
    root.title('Issue Book')
    root.geometry("400x400+480+180")
    root.resizable(False, False)
    name = Label(root, text='ISSUE ', font='Helvetica 30 bold')
    branch = Label(root, text='BOOK', font='Helvetica 30 bold')
    sid = Label(root, text='MEMBER ID')
    no = Label(root, text='BOOK ID')
    issue = Label(root, text='ISSUE DATE')
    exp = Label(root, text='RETURN DATE')
    global e1, b, b1
    e1 = Entry(root, width=25)
    global e4
    e4 = Entry(root, width=25)
    global com1y, com1m, com1d, com2y, com2m, com2d
    com1y = Combobox(root, value=y, width=5)
    com1m = Combobox(root, value=month, width=5)
    com1d = Combobox(root, value=d, width=5)
    com2y = Combobox(root, value=y, width=5)
    com2m = Combobox(root, value=month, width=5)
    com2d = Combobox(root, value=d, width=5)
    now = datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month - 1])
    com1d.set(now.day)
    com2y.set(now.year)
    com2m.set(month[now.month - 1])
    com2d.set(now.day)
    b = Button(root, height=2, width=21, text=' ISSUE BOOK ', command=issuebooks)
    b1 = Button(root, height=2, width=21, text=' CLOSE ', command=closebooks)
    name.place(x=55, y=30)
    branch.place(x=225, y=30)
    sid.place(x=70, y=130)
    no.place(x=70, y=170)
    issue.place(x=70, y=210)
    exp.place(x=70, y=240)
    e1.place(x=180, y=130)
    e4.place(x=180, y=170)
    com1y.place(x=180, y=210)
    com1m.place(x=230, y=210)
    com1d.place(x=280, y=210)
    com2y.place(x=180, y=240)
    com2m.place(x=230, y=240)
    com2d.place(x=280, y=240)
    b.place(x=178, y=270)
    b1.place(x=178, y=312)
    root.mainloop()
    pass


def returnbooks():
    connectdb()
    q = 'SELECT exp FROM BookIssue WHERE Book_id="%s"'
    cur.execute(q % (e4.get()))
    e = cur.fetchone()
    e = str(e[0])
    i = datetime.date.today()
    e = datetime.date(int(e[:4]), int(e[5:7]), int(e[8:10]))
    if i <= e:
        a = 'DELETE FROM BookIssue WHERE serial="%s"'
        cur.execute(a % e4.get())
        con.commit()
    else:
        t = str((i - e) * 10)
        messagebox.showinfo("Fine", t[:4] + ' Fine ')
    root.destroy()
    closedb()
   # libr()
    pass


def returnbook():
    global root
    # win.destroy()
    root = Tk()
    root.title('Return Book')
    root.geometry("400x400+480+180")
    root.resizable(False, False)
    ret = Label(root, text='RETURN ', font='Helvetica 30 bold')
    book = Label(root, text='BOOK', font='Helvetica 30 bold')
    s_id = Label(root, text = 'STUDENT ID')
    no = Label(root, text='BOOK ID')
    date = Label(root, text='RETURN DATE')
    exp = Label(root, text='')
    global b, b1, b2
    global e4,e5
    e4 = Entry(root, width=25)
    e5 = Entry(root, width=25)
    global com1y, com1m, com1d, com2y, com2m, com2d
    com1y = Combobox(root, value=y, width=5)
    com1m = Combobox(root, value=month, width=5)
    com1d = Combobox(root, value=d, width=5)
    '''com2y=Combobox(win,width=5)
    com2m=Combobox(win,width=5)
    com2d=Combobox(win,width=5)'''
    now = datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month - 1])
    com1d.set(now.day)

    b = Button(root, height=2, width=21, text=' RETURN BOOK ', command=returnbooks)
    b1 = Button(root, height=2, width=21, text=' CLOSE ', command=closebooks)
    ret.place(x=55, y=30)
    book.place(x=225, y=30)
    s_id.place(x=70, y=80)
    no.place(x=70, y=120)
    date.place(x=70, y=160)
    exp.place(x=70, y=200)
    e5.place(x=180, y=80)
    e4.place(x=180, y=120)
    com1y.place(x=180, y=160)
    com1m.place(x=230, y=160)
    com1d.place(x=280, y=160)
    '''com2y.place(x=180,y=200)
    com2m.place(x=230,y=200)
    com2d.place(x=280,y=200)'''
   # b2.place(x=178, y=158)
    b.place(x=178, y=200)
    b1.place(x=178, y=242)
    root.mainloop()
    pass



def issuedbook():
    connectdb()
    q = 'SELECT * FROM BookIssue'
    cur.execute(q)
    details = cur.fetchall()
    if len(details) != 0:
        root = Tk()
        root.title('View Books')
        root.geometry("800x300+270+180")
        root.resizable(False, False)
        treeview = Treeview(root, columns=("Student ID", "Serial No", "Issue Date", "Expiry Date"), show='headings')
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Serial No", text="Serial No")
        treeview.heading("Issue Date", text="Issue Date")
        treeview.heading("Expiry Date", text="Expiry Date")
        treeview.column("Student ID", anchor='center')
        treeview.column("Serial No", anchor='center')
        treeview.column("Issue Date", anchor='center')
        treeview.column("Expiry Date", anchor='center')
        index = 0
        iid = 0
        for row in details:
            treeview.insert("", index, iid, value=row)
            index = iid = index + 1
        treeview.pack()
        root.mainloop()
    else:
        messagebox.showinfo("Books", "No Book Issued")
    pass

def closedb():
    global con, cur
    cur.close()
    con.close()
    pass



btn1 = Button(root, text="Add Book Details", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=addbook)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=deletebook)
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=viewbook)
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=issuebook)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=returnbook)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="Issued Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=issuedbook)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
root.mainloop()
