#weight gain
from tkinter import *
from PIL import Image, ImageTk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()
root.title('DIET PLANS')
root.geometry('1300x700')
global img1
canvas = Canvas(root, bg="blue")
canvas.pack(side=LEFT, fill=BOTH, expand=True)
frame = Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame, anchor='nw')
img1 = Image.open('weight gain.png')
img1 = img1.resize((920, 650),Image.ADAPTIVE)
img1 = ImageTk.PhotoImage(img1)
imageLabel = Label(frame, image=img1)
imageLabel.grid(row=0, column=0, sticky=W)

text="There is no shortcut to gaining weight. You need to maintain a healthy diet, include premium quality fitness supplements like – whey protein, creatine, or mass gainer supplement, drink enough water, and do daily workouts. To maintain your weight after gaining it, you should have at least 0.8 g/ kg protein per body weight."
Label(frame, text=text, wraplength=350, font="helvetica 14").grid(row=0, column=2, sticky=W)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
frame.bind("<Configure>", on_configure)

root.mainloop()
