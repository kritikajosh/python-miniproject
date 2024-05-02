import mysql.connector
from tkinter import *
from tkinter import messagebox

conn=mysql.connector.connect(host="localhost",user="root",password="",database="prp")
cur=conn.cursor()
root=Tk()
root.title('SIGN UP PAGE')
root.geometry('500x500')

def signup():
    new=newuser.get()
    password1=password.get()
    confirmed=confirmPass.get()
    goal=option1.get()
    if new!=None and password1!=None:
        query="insert into users(username,password) values(%s,%s)"
        val=(new,password1)
        cur.execute(query,val)
        conn.commit()
        messagebox.showinfo(message='RECORD INSERTED')
        root.destroy()
        import dashboard
        root.mainloop()
        
        exit()
    else:
        messagebox.showinfo(message="please enter all fields")
def login():
    root.destroy()
    import login
    exec(open('login.py').read())
option1=StringVar(root,'0')
usernameLabel=Label(root,text='Enter Username:').grid(row=2,column=1,sticky=W)
passwordLabel=Label(root,text='Enter Password:').grid(row=3,column=1,sticky=W)
confirmLabel=Label(root,text='Confirm Password:').grid(row=4,column=1,sticky=W)
newuser=Entry(root,width=30)
newuser.grid(row=2,column=2)
password=Entry(root,width=30,show='*')
password.grid(row=3,column=2)
Label(root,text='Remember this password the next time you login!').grid(row=5,column=1,sticky=W)
confirmPass=Entry(root,show='*',width=30)
confirmPass.grid(row=4,column=2)
goalsLabel=Label(root,text='Select 1 goal for now').grid(row=6,column=1)
c1=Radiobutton(root,text='Lose weight',variable=option1,value='1')
c1.grid(row=6,column=2)
c2=Radiobutton(root,text='High protein',variable=option1,value='2')
c2.grid(row=7,column=2)
c3=Radiobutton(root,text='Gain weight',variable=option1,value='3')
c3.grid(row=8,column=2)
c4=Radiobutton(root,text='Maintain weight',variable=option1,value='4')
c4.grid(row=9,column=2)
submit=Button(root,text="SUBMIT",command=signup).grid(row=10,column=1)
Label(root,text='Already have an account?').grid(row=12,column=1)
login=Button(root,text="LOGIN",command=login).grid(row=14,column=1)
root.mainloop()
