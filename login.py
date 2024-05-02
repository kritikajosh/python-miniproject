import mysql.connector
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
con=mysql.connector.connect(host="localhost",user="root",password="",database="prp")
cur=con.cursor()
root=Tk()
root.columnconfigure(2,weight=2)
root.columnconfigure(1,weight=1)
root.geometry('1000x1000')
root.title('Home')
def login():
    user=username.get()
    password=password1.get()
    goal=option1.get()
    if user==None or password==None or goal==None:
        messagebox.showinfo(message='Please enter all fields')
    else:
        try:
            check="select * from users"
            cur.execute(check)
            result=cur.fetchall()
            for row in result:
                if row[3]==0:
                    query="insert into users(goal) values(%s)"
                    val=(goal,)
                    cur.execute(query,val)
                    con.commit()
                if row[1]==user and row[2]==password:
                    root.destroy()
                    openHome()
                    
                else:
                    raise Exception('No such username')
        except Exception as e:
            messagebox.showerror(message=e)
def openHome():
    import dashboard
    exec(open('dashboard.py').read())
def signup():
    root.destroy()
    import signup
    exec(open('signup.py').read())
option1=StringVar(root,'0')
usernameLabel=Label(root,text='Enter Username:').grid(row=2,column=1,sticky=W)
passwordLabel=Label(root,text='Enter Password:').grid(row=3,column=1,sticky=W)
username=Entry(root)
username.grid(row=2,column=1)
password1=Entry(root,show='*')
password1.grid(row=3,column=1)
goalsLabel=Label(root,text='Select 1 goal for now').grid(row=6,column=1,sticky=W)
c1=Radiobutton(root,text='Lose weight',variable=option1,value='1')
c1.grid(row=6,column=1)
c2=Radiobutton(root,text='High protein',variable=option1,value='2')
c2.grid(row=7,column=1)
c3=Radiobutton(root,text='Gain weight',variable=option1,value='3')
c3.grid(row=8,column=1)
c4=Radiobutton(root,text='Maintain weight',variable=option1,value='4')
c4.grid(row=9,column=1)
login=Button(root,text="LOGIN",command=login).grid(row=11,column=1,sticky=W)
l1=Label(root,text="Don't have an account?").grid(row=12,column=1,sticky=W)
signup_button=Button(root,text="SIGN UP",command=signup).grid(row=13,column=1,sticky=W)
pic=PhotoImage(file='butterfly.png')
img1=Image.open('health fitness cartoon.png')
img1=img1.resize((250,200))
img1=ImageTk.PhotoImage(img1)
imageLabel=Label(root,image=img1)
imageLabel.grid(row=2,column=2,sticky=W)
root.iconphoto(False,pic)
root.mainloop()
