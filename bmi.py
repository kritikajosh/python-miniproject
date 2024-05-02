#bmi calc
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk('bmi')
root.geometry('500x500')
def check():
    goal=option1.get()
    height=userheight.get()
    height=int(height)/100
    weight=userweight.get()
    weight=int(weight)
    bmi=weight/(height*height)
    messagebox.showinfo(message=("your bmi is ",bmi))
option1=StringVar(root,'0')
goalsLabel=Label(root,text='Select 1 goal for now').grid(row=1,column=3)
c1=Radiobutton(root,text='Lose weight',variable=option1,value='1')
c1.grid(row=1,column=4)
c2=Radiobutton(root,text='High protein',variable=option1,value='2')
c2.grid(row=2,column=4)
c3=Radiobutton(root,text='Gain weight',variable=option1,value='3')
c3.grid(row=3,column=4)
c4=Radiobutton(root,text='Maintain weight',variable=option1,value='4')
c4.grid(row=4,column=4)
heightLabel=Label(root,text='Enter height(in centimeters)').grid(row=5,column=3)
weightLabel=Label(root,text='Enter weight(in kgs)').grid(row=7,column=3)
userheight=Entry(root,width=30)
userheight.grid(row=5,column=4)
userweight=Entry(root,width=30)
userweight.grid(row=7,column=4)
submit=Button(root,text='SUBMIT',command=check).grid(row=10,column=3)
progress = ttk.Progressbar(root, orient = HORIZONTAL,length = 100, mode = 'indeterminate')
progress.pack()
root.mainloop()
