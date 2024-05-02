from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from time import strftime 
import mysql.connector
import subprocess

conn=mysql.connector.connect(host="localhost",user="root",password="",database="prp")
cur=conn.cursor()

def diet():
    if goal==1:
        from weight_loss import root
        root.mainloop()
    if goal==2:
        from high_protein import root
        root.mainloop()
    if goal==3:
        from weight_gain import root
        root.mainloop()
    if goal==4:
        from maintain import root
        root.mainloop()
def workot():
    if goal==1:
        import loss_workout
        exec(open('gain.py').read())
    if goal==3:
        import gain
        exec(open('gain.py').read())
    if goal==4:
        import maintain_weight
        exec(open('gain.py').read())
def bmi():
    import bmi
    exec(open('bmi.py').read())
root1 = Tk() 
root1.title('Menu Demonstration') 
root1.geometry('1000x1000')
menubar = Menu(root1)  

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='My routines', menu = file) 
file.add_command(label ='Diet', command = diet) 
file.add_command(label ='Workout', command = workot)
file.add_separator() 

edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Goals', menu = edit) 
edit.add_command(label ='View goals', command = None)
edit.add_command(label ='Update goals', command = None) 
 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='My profile', menu = help_) 
help_.add_command(label ='BMI', command = bmi)
help_.add_separator() 
help_.add_command(label ='Exit', command = root1.destroy)

img1=Image.open('download.png')
img1=img1.resize((850,550))
img1=ImageTk.PhotoImage(img1)
imageLabel=Label(root1,image=img1)
imageLabel.place(x=100,y=100)

pic=PhotoImage(file='butterfly.png')
root1.iconphoto(False,pic)
root1.config(menu = menubar) 
root1.mainloop() 
