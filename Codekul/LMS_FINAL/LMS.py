from tkinter import *
from PIL import ImageTk, Image  # PIL -> Pillow
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime
global aa

def connectdb():
    global con, cur, enter
    # Enter your username and password of MySQL
    con = p.connect(host="127.0.0.1", user="root", passwd="root")
    cur = con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS Library')
    cur.execute('USE Library')
    enter=1

    '''if enter == 1:
        l = 'CREATE TABLE IF NOT EXISTS member_details(name varchar(20) NOT NULL,userid varchar(10) PRIMARY KEY,password varchar(20) NOT NULL,PRN ,branch varchar(20),mobile int(10) UNIQUE);'
        b = 'CREATE TABLE IF NOT EXISTS Books(ISBN_NO int Primary key,Book_Name varchar(100) NOT NULL,Author varchar(30) NOT NULL, Language varchar(100) NOT NULL,Book_id varchar(8) NOT NULL, Publication varchar(50) Not Null,Publication_year int, No_Of_Copies int,Department varchar(30), Shelf_No int);'
        i = 'CREATE TABLE IF NOT EXISTS BookIssue(stdid varchar(20) UNIQUE NOT NULL,Book_id varchar(10) NOT NULL, Book_Name varchar(50) NOT NULL,issue date,exp date)'
       # cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        enter = enter + 1
    #query = 'SELECT * FROM Login'
    #cur.execute(query)
    pass'''


month=['January','February','March','April','May','June','July','August','September','October','November','December']
y = list(range(2015, 2040))
d = list(range(1,32))

#
#---------------------------------------------CLOSE BOOKS-------------------------------------

def closebooks():
    global root
   # root.destroy()
    libr()
#----------------------------------------------ADD BOOKS-------------------------------------
def addbooks():
    connectdb()
    global root, cur, con
    q = 'SELECT Book_id FROM Books WHERE Book_id = "%s";'
    cur.execute(q % (e4.get()))
    details = cur.fetchall()
    if len(details) != 0:
        u= ' UPDATE books SET Available_books = Available_books + "%i" WHERE Book_id = "%s";'
        cur.execute(u % (int(e9.get()),e4.get()))
        con.commit()
        messagebox.showinfo("Book", "Book Added")
        closedb()
        # libr()
        closebooks()
    else:
        e11 = int(e9.get())
        q = 'INSERT INTO Books VALUE("%i","%s","%s","%s","%s","%s","%s","%i","%i", "%i","%i")'
        #global root,cur, con
        cur.execute(q % (int(e1.get()), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(),e7.get(), int(e8.get()), int(e9.get()),int(e11), int(e10.get())))
        con.commit()
        #root.destroy()
        messagebox.showinfo("Book", "Book Added")
        closedb()
        #libr()
        closebooks()
        #root.mainloop()

def addbook():
    global root
    root.destroy()
    root = Tk()
    root.title('Add Book')
    root.geometry("750x350")
    root.resizable(False, False)
    isbn = Label(root, text='ISBN No.')
    tit = Label(root, text='Book TITLE')
    auth = Label(root, text='AUTHOR')
    dept = Label(root, text='Department')
    lang = Label(root, text='LANGUAGE')
    Book_id = Label(root, text='BOOK ID')
    pub = Label(root, text='PUBLICATION')
    pub_yr = Label(root, text='YEAR OF PUBLICATION')
    cop = Label(root, text='COPIES ADDED')
    shelf_no = Label(root, text='SHELF No.')
   # global e11
   # e11=0
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
    Book_id.place(x=70, y=170)
    dept.place(x=70, y=210)
    lang.place(x=400, y=50)
    pub.place(x=400, y=90)
    pub_yr.place(x=400, y=130)
    cop.place(x=400, y=170)
    shelf_no.place(x=400, y=210)
    e1.place(x=180, y=50)
    e2.place(x=180, y=90)
    e3.place(x=180, y=130)
    e4.place(x=180, y=170)
    e5.place(x=180, y=210)
    e6.place(x=550, y=50)
    e7.place(x=550, y=90)
    e8.place(x=550, y=130)
    e9.place(x=550, y=170)
    e10.place(x=550, y=210)
    b.place(x=100, y=250)
    b1.place(x=450, y=250)
    root.mainloop()

#-----------------------------------------------------------------------------------

#----------------------DELETE BOOKS-----------------------------------------------

def deletebooks():
    connectdb()
    q = 'SELECT Book_id FROM Books WHERE Book_id = "%s";'
    cur.execute(q % (e1.get()))
    details = cur.fetchall()
    if len(details)!=0:
        if e2.get() == 'Library@7':
            q = 'DELETE FROM Books WHERE Book_id="%s"'
            cur.execute(q % (e1.get()))
            con.commit()
            #root.destroy()
            messagebox.showinfo("Delete", "Book Deleted")
            closedb()
            libr()
        else:
            messagebox.showinfo("Error", "Incorrect Password")
            closedb()
    else:
        messagebox.showinfo("Error", "Book Not Found")
        closedb()


def deletebook():
    global root
    root.destroy()
    root = Tk()
    root.title('Delete Book')
    root.geometry("400x350+480+180")
    root.resizable(False, False)

    usid = Label(root, text='BOOK ID')
    paswrd = Label(root, text='PASSWORD')
    global e1
    e1 = Entry(root)
    global e2, b2
    e2 = Entry(root)
    #img = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\bt6.png")
    b1 = Button(root, height=2, width=17, text=' DELETE ', command=deletebooks)
    b2 = Button(root, height=2, width=17, text=' CLOSE ', command=closebooks)
    usid.place(x=80, y=100)
    paswrd.place(x=70, y=140)

    e1.place(x=180, y=100)
    e2.place(x=180, y=142)
    b1.place(x=180, y=180)
    b2.place(x=180, y=230)
    root.mainloop()
#----------------------------------------------------------------------------------

#------------------VIEW BOOKS-------------------------------------------------------

def viewbook():
    root = Tk()
    root.title('View Books')
    root.geometry("1000x300+10+20")
    root.resizable(True, True)
    treeview = Treeview(root, columns=("ISBN_No", "Book_Name", "Author", "Book_id", "Department", "Language", "Publication", "Publication_Year", "Copies_added", "Shelf_No"), show='headings')
    treeview.heading("ISBN_No", text="ISBN No")
    treeview.heading("Book_Name", text="Book Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Book_id", text="Book Id")
    treeview.heading("Department", text="Department")
    treeview.heading("Language", text="Language")
    treeview.heading("Publication", text="Publication")
    treeview.heading("Publication_Year", text="Publication Year")
    treeview.heading("Copies_added", text="Copies Added")
   # treeview.heading("Copies_Available", text="Copies Available")
    treeview.heading("Shelf_No", text="Shelf No")
    treeview.column("ISBN_No", anchor='center')
    treeview.column("Book_Name", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Book_id", anchor='center')
    treeview.column("Department", anchor='center')
    treeview.column("Language", anchor='center')
    treeview.column("Publication", anchor='center')
    treeview.column("Publication_Year", anchor='center')
    treeview.column("Copies_added", anchor='center')
    #treeview.column("Copies_Available", anchor='center')
    treeview.column("Shelf_No", anchor='center')
    index = 0
    iid = 0
    connectdb()
    q = 'SELECT * FROM books;'
    cur.execute(q)
    details = cur.fetchall()
    for row in details:
        treeview.insert("", index, iid, value=row)
        index = iid = index + 1
    treeview.pack()
    #root.destroy()
    closedb()
    libr()
#----------------------------------------------------------------------------------

#------------------ISSUE BOOKS----------------------------------------------------

def issuebooks():
    connectdb()
    q1 = 'SELECT Book_id FROM Books WHERE Book_id = "%s";'
    cur.execute(q1 % (e4.get()))
    det = cur.fetchall()
    q = 'SELECT member_id FROM member_details WHERE member_id = "%s";'
    cur.execute(q % (e1.get()))
    details = cur.fetchall()
    if len(details) != 0:
        if len(det) != 0:
            q = 'INSERT INTO BookIssue VALUE("%s","%s","%s","%s");'
            i = datetime.datetime(int(com1y.get()), month.index(com1m.get()) + 1, int(com1d.get()))
            e = datetime.datetime(int(com2y.get()), month.index(com2m.get()) + 1, int(com2d.get()))
            i = i.isoformat()
            e = e.isoformat()
            cur.execute(q % (e1.get(), e4.get(), i, e))
            con.commit()
            u = ' UPDATE books SET Available_books = Available_books - 1 WHERE Book_id = "%s";'
            cur.execute(u % (e4.get()))
            con.commit()
            #root.destroy()
            messagebox.showinfo("Book", "Book Issued")
            #root.destroy()
            closedb()
           # libr()
            closebooks()
        else:
            messagebox.showinfo("Message", "Book no Found")
            closedb()
    else:
        messagebox.showinfo("Error", "Unidentified Member")
        closedb()

    '''p = 'select member_id from member_details where member_id ="%s";'
    cur.execute(p % (e1.get()))
    con.commit()
    c = 'select copies_Available from books where book_id = "%s";'
    cur.execute(c % (e4.get()))
    con.commit()
    if (str(e1.get) in p) and ((e4.get()) > 0):
        q = 'INSERT INTO BookIssue VALUE("%s","%s","%s","%s")'
        i = datetime.datetime(int(com1y.get()), month.index(com1m.get()) + 1, int(com1d.get()))
        e = datetime.datetime(int(com2y.get()), month.index(com2m.get()) + 1, int(com2d.get()))
        i = i.isoformat()
        e = e.isoformat()
        cur.execute(q % (e1.get(), e4.get(), i, e))
        con.commit()
        root.destroy()
        messagebox.showinfo("Message", "Book Issued")
        closedb()
       # root.mainloop()
        libr()
    else:
        messagebox.showinfo("Message", "This id is not in our database")'''




def issuebook():
    global root
    root.destroy()
    root = Tk()
    root.title('Issue Book')
    root.geometry("400x400+480+180")
    root.resizable(False, False)
    name = Label(root, text='ISSUE Book ', font='Helvetica 20 bold')
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
    b = Button(root, height=1, width=10, text=' ISSUE BOOK ', command=issuebooks)
    b1 = Button(root, height=1, width=10, text=' CLOSE ', command=closebooks)
    name.place(x=120, y=30)
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
    b.place(x=70, y=290)
    b1.place(x=200, y=290)
    root.mainloop()
#---------------------------------------------------------------------------------

#----------------------------------RETURN BOOKS------------------------------------

def returnbooks():
    connectdb()
    q = 'SELECT exp FROM BookIssue WHERE Book_id="%s" AND stdid ="%s";'
    cur.execute(q % (e4.get(),e5.get()))
    e = cur.fetchone()
    e = str(e[0])
    i = datetime.date.today()
    e = datetime.date(int(e[:4]), int(e[5:7]), int(e[8:10]))

    if i <= e:
        a = 'DELETE FROM BookIssue WHERE Book_id="%s"'
        cur.execute(a % e4.get())
        con.commit()
        messagebox.showinfo("Acknowledgement","Book Successfully Returned")
    else:
        t = str((i - e) * 10)
        messagebox.showinfo("Fine",'Fine : Rs '+ t[:4])
        a = 'DELETE FROM BookIssue WHERE Book_id="%s"'
        cur.execute(a % e4.get())
        con.commit()
        messagebox.showinfo("Acknowledgement", "Book Successfully Returned")
    #root.destroy()
    closedb()
    #libr()
    closebooks()



def returnbook():
    global root
    root.destroy()
    root = Tk()
    root.title('Return Book')
    root.geometry("400x400+480+180")
    root.resizable(False, False)
    ret = Label(root, text='RETURN ', font='Helvetica 30 bold')
    book = Label(root, text='BOOK', font='Helvetica 30 bold')
    stdid = Label(root, text = 'STUDENT ID')
    Book_id = Label(root, text='BOOK ID')
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
    stdid.place(x=70, y=80)
    Book_id.place(x=70, y=120)
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
#---------------------------------------------------------------------------------


#----------------------------------ISSUED BOOKS-------------------------------------

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
        treeview = Treeview(root, columns=("member_id", "Book_id", "Issue_Date", "Expiry_Date"), show='headings')
        treeview.heading("member_id", text="Member ID")
        treeview.heading("Book_id", text="Book ID")
        treeview.heading("Issue_Date", text="Issue Date")
        treeview.heading("Expiry_Date", text="Expiry Date")
        treeview.column("member_id", anchor='center')
        treeview.column("Book_id", anchor='center')
        treeview.column("Issue_Date", anchor='center')
        treeview.column("Expiry_Date", anchor='center')
        index = 0
        iid = 0
        for row in details:
            treeview.insert("", index, iid, value=row)
            index = iid = index + 1
        treeview.pack()
        root.mainloop()
    else:
        messagebox.showinfo("Books", "No Book Issued")


def closedb():
    global con, cur
    cur.close()
    con.close()


#---------------------------------------------ADMIN_LOGIN-------------------------------------------------------------------------------

def loginadmin():
    if e1.get()=='admin' and e2.get()=='admin':
        admin();
    else:
        messagebox.showerror('Library System', 'Your ID or Password is not Valid')

def admin():
    window.withdraw()
    global root,b1,b2,b3,b4,cur,con
    root=Tk()
    root.title('Admin')
    root.geometry("400x400+480+180")
    root.resizable(False,False)
    b1=Button(root, height=2,width=25,text=' Add User ',command=adduser)
    b2=Button(root, height=2,width=25,text=' View User ',command=viewuser)
    b3=Button(root, height=2,width=25,text=' Delete User ',command=deleteuser)
    b4=Button(root, height=2,width=25,text=' LogOut ',command=logout)
    b1.place(x=110,y=70)
    b2.place(x=110,y=120)
    b3.place(x=110,y=170)
    b4.place(x=110,y=220)
    root.mainloop()

def logout():
    root.destroy()
    try:
        closedb()
    except:
        print("Logged Out")
    home()

'''def closedb():
    global con,cur
    cur.close()
    con.close()'''

def adduser():
    global root
    root.destroy()
    root=Tk()
    root.title('Add User')
    root.geometry("400x450+480+180")
    root.resizable(False,False)
    name=Label(root,text='NAME')
    password=Label(root,text='PASSWORD')
    PRN=Label(root,text='PRN')
    branch=Label(root,text='DEPARTMENT')
    mobile=Label(root,text='MOBILE NO.')
    member_id=Label(root, text='MEMBER_ID')
    global e1,b
    e1=Entry(root,width=25)
    global e2
    e2=Entry(root,width=25)
    global e3
    e3=Entry(root,width=25)
    global e4
    e4=Entry(root,width=25)
    global e5
    e5 = Entry(root, width=25)
    global e6
    e6 = Entry(root, width=25)
    b=Button(root, height=2,width=21,text=' ADD USER ',command=addusers)
    b1=Button(root, height=2,width=21,text=' CLOSE ',command=closeusers)
    name.place(x=70,y=100)
    password.place(x=70,y=140)
    PRN.place(x=70,y=180)
    branch.place(x=70,y=220)
    mobile.place(x=70,y=260)
    member_id.place(x=70,y=300)
    e1.place(x=180,y=100)
    e2.place(x=180,y=140)
    e3.place(x=180,y=180)
    e4.place(x=180,y=220)
    e5.place(x=180,y=260)
    e6.place(x=180,y=300)
    b.place(x=178,y=340)
    b1.place(x=178,y=383)
    root.mainloop()

def addusers():
    connectdb()
    q='INSERT INTO member_details VALUE("%s","%i","%s","%i","%s","%s")'
    global con,cur
    cur.execute(q%(e1.get(),int(e3.get()),e4.get(),int(e5.get()),e6.get(),e2.get()))
    con.commit()
    root.destroy()
    messagebox.showinfo("User", "User Added")
    closedb()
    admin()

def closeusers():
    global root
    root.destroy()
    admin()

def viewuser():
    root=Tk()
    root.title('View User')
    root.geometry("800x300+270+180")
    root.resizable(False,False)
    treeview = Treeview(root,columns=("name","PRN","branch","mobile","member_id"),show='headings')
    treeview.heading("name", text="Name")
    treeview.heading("PRN", text="PRN")
    treeview.heading("branch", text="Branch")
    treeview.heading("mobile", text="Mobile No")
    treeview.heading("member_id", text="Member ID")
    treeview.column("name", anchor='center')
    treeview.column("PRN", anchor='center')
    treeview.column("branch", anchor='center')
    treeview.column("mobile", anchor='center')
    treeview.column("member_id", anchor='center')
    index=0
    iid=0
    connectdb()
    q="SELECT * FROM member_details"
    cur.execute(q)
    details=cur.fetchall()
    for row in details:
        treeview.insert("",index,iid,value=row)
        index=iid=index+1
    treeview.pack()
    root.mainloop()
    closedb()


def deleteuser():
    global root
    root.destroy()
    root=Tk()
    root.title('Delete user')
    root.geometry("400x400+480+180")
    root.resizable(False,False)
    usid=Label(root,text='USER ID')
    paswrd=Label(root,text='ADMIN \n PASSWORD')
    global e1
    e1=Entry(root)
    global e2,b2
    e2=Entry(root)
    b1=Button(root, height=2,width=17,text=' DELETE ',command=deleteusers)
    b2=Button(root, height=2,width=17,text=' CLOSE ',command=closeusers)
    usid.place(x=80,y=100)
    paswrd.place(x=70,y=140)
    e1.place(x=180,y=100)
    e2.place(x=180,y=142)
    b1.place(x=180,y=180)
    b2.place(x=180,y=230)
    root.mainloop()

def deleteusers():
    connectdb()
    if e2.get()=='admin':
        q='DELETE FROM member_details WHERE member_id="%i"'
        cur.execute(q%(int(e1.get())))
        con.commit()
        root.destroy()
        messagebox.showinfo("Delete", "User Deleted")
        closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        closedb()

############################################################################################################################
def loginlibr():
    connectdb()
    global root,aa
    root = Tk()
    var1=e1.get()
    var2 = e2.get()
    cur.execute("select * from member_details where member_id='"+var1+"'and password='"+var2+"'")
    con.commit()
    ab=cur.fetchone()
    if ab != None:
        aa =ab
        messagebox.showinfo('Library System', 'LogIn successful')
        libr()
    else:
        messagebox.showerror('Library System', 'Your ID or Password is not Valid')

#*************************************************************************************************************************************

def libr():
    window.withdraw()
    global root
    root.destroy()
    root=Tk()
    root.title("My Library")
    root.iconbitmap("aa.ico")
    root.minsize(width=400, height=400)
    root.geometry("750x400")
    root.resizable(False, False)
    under_fm = Frame(root, height=750, width=400, bg='#fff')
    under_fm.place(x=0, y=0)
    fm2 = Frame(root, bg='#0f624c', bd=6)
    fm2.place(relx=0.20, rely=0.05, relwidth=0.55, relheight=0.1)
       #  lgo=Canvas(fm2,bg='#0f624c',height=200,width=100,bd=4,relief='flat')
       #  lgo.place(x=0,y=0)
   # pic_0 = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\library.png")

    lbb = Label(fm2, bg='#0f624c')
    lbb.place(x=15, y=5)
    #       ig = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\library.png")
    #        lbb.config(image=pic_0)
    lb3 = Label(fm2, text=" Welcome to GuruKul Library", bg='#0f624c', fg='white', font=('Courier', 14))
    lb3.place(relx=0, rely=0.0, relwidth=1, relheight=1)

    # ----------------------------name------------------------

    name = Label(root, text="Name : ", bg='#fff', fg="black", font=('Arial', 10, 'bold'))
    name.place(x=5, y=83)
    name1 = Label(root, text=aa[0], fg='black', bg='#fff', font=('Arial', 10, 'bold'))
    name1.place(x=60, y=83)
    # ------------------------date-------------------------
    today = datetime.date.today()
    dat = Label(root, text='Date : ', bg='#fff', fg='black', font=('Arial', 10, 'bold'))
    dat.place(x=590, y=83)
    dat2 = Label(root, text=today, bg='#fff', fg='black', font=('Arial', 10, 'bold'))
    dat2.place(x=640, y=83)
    # cur()

    # ----------------------------MENU BUTTONS--------------------------------

    # pic_1 = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\bt1.png")
    btn1 = Button(root, text=" Add Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=addbook)
    btn1.place(relx=0.1, rely=0.35, relwidth=0.25, relheight=0.1)
#    pic_1 = PhotoImage(file="bt1.png")
#    btn1.config(image=pic_1,compound=LEFT)
#    s_pic_1 =pic_1.subsample(1,1)
 #   btn1.config(image=s_pic_1)


    # pic_2 = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\bt5.png")
    btn2 = Button(root, text=" Delete Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=deletebook)
    btn2.place(relx=0.1, rely=0.45, relwidth=0.25, relheight=0.1)


    #  pic_3 = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\bt3.png")
    btn3 = Button(root, text=" View Book List", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=viewbook)
    btn3.place(relx=0.1, rely=0.55, relwidth=0.25, relheight=0.1)


    # pic_4 = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\bt2.png")
    btn4 = Button(root, text=" Issue Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=issuebook)
    btn4.place(relx=0.1, rely=0.65, relwidth=0.25, relheight=0.1)

    # pic_5 = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\bt4.png")
    btn5 = Button(root, text=" Return Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=returnbook)
    btn5.place(relx=0.1, rely=0.75, relwidth=0.25, relheight=0.1)


    #  pic_6 = PhotoImage(file=r"C:\Users\gauta\Desktop\Codekul\bt6.png")
    btn6 = Button(root, text=" Issued Book", bg='#DD8E7E', fg='white', font=('Comic Sans', 12), command=issuedbook)
    btn6.place(relx=0.1, rely=0.85, relwidth=0.25, relheight=0.1)


    btn7 = Button(root, height=1, width=10, text=' LogOut ',bg= '#fff', command=logout)
    btn7.place(x=5, y=110)
    root.mainloop()

#*************************************************************************************************************************************




#---------------------------------------------------------------------------------------------------------------------------------


def login_staff():
    try:
        global window, b1, e1, e2, con, cur, win
        window.destroy()
        window = Tk()
        window.title('Welcome')
        window.resizable(False, False)
        window.geometry("400x400+480+180")
        # wel=Label(window,text='LIBRARY',font='Helvetica 28 bold')
        # lib=Label(window,text='MANAGEMENT',font='Helvetica 28 bold')
        usid = Label(window, text='USER ID')
        paswrd = Label(window, text='PASSWORD')
        e1 = Entry(window, width=22)
        e2 = Entry(window, width=22)
        b1 = Button(window, text=' LOGIN AS STAFF', height=2, width=20, command=loginlibr)
      #  b2 = Button(window, text=' LOGIN AS ADMIN ', height=2, width=20, command=loginadmin)
        # wel.place(x=160,y=20)
        # lib.place(x=110,y=70)
        usid.place(x=70, y=100)
        paswrd.place(x=70, y=140)
        e1.place(x=180, y=100)
        e2.place(x=180, y=140)
        b1.place(x=175, y=180)
       # b2.place(x=175, y=225)
        window.mainloop()
    except Exception:
        window.destroy()


def login_admin():
    try:
        global window, b2, e1, e2, con, cur, win
        window.destroy()
        window = Tk()
        window.title('Welcome')
        window.resizable(False, False)
        window.geometry("400x400+480+180")
        # wel=Label(window,text='LIBRARY',font='Helvetica 28 bold')
        # lib=Label(window,text='MANAGEMENT',font='Helvetica 28 bold')
        usid = Label(window, text='USER ID')
        paswrd = Label(window, text='PASSWORD')
        e1 = Entry(window, width=22)
        e2 = Entry(window, width=22)
        #b1 = Button(window, text=' LOGIN AS STAFF', height=2, width=20, command=loginlibr)
        b2 = Button(window, text=' LOGIN AS ADMIN ', height=2, width=20, command=loginadmin)
        # wel.place(x=160,y=20)
        # lib.place(x=110,y=70)
        usid.place(x=70, y=100)
        paswrd.place(x=70, y=140)
        e1.place(x=180, y=100)
        e2.place(x=180, y=140)
        b2.place(x=175, y=180)
        window.mainloop()
    except Exception:
        window.destroy()



def home():
    try:
        global window,b1,b2,con,cur,win
        window=Tk()
        window.title('Welcome')
        window.resizable(False,False)
        window.geometry("450x400+480+180")
        b1=Button(window,text=' LOGIN AS STAFF' ,height=2,width=20,command=login_staff)
        b2=Button(window,text=' LOGIN AS ADMIN ', height=2,width=20,command=login_admin)
        b1.place(x=50,y=180)
        b2.place(x=250,y=180)
        window.mainloop()
       # window.destroy()
    except Exception:
        window.destroy()
enter=1
home()