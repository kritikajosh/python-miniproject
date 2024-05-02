#high protein
from tkinter import *
from PIL import Image, ImageTk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()
root.title('DIET PLANS')
root.geometry('1300x700')

canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
frame = Frame(canvas, )
canvas.create_window((0, 0), window=frame, anchor='nw')
img1 = Image.open('protein.png')
img1 = img1.resize((920, 650))
img1 = ImageTk.PhotoImage(img1)
imageLabel = Label(frame, image=img1)
imageLabel.grid(row=0, column=0, sticky=W)

text='Women need at least 50 grams of protein a day -- men about 60 grams per day. With a high-protein diet, it can be much more than that. This extra protein can come from beans, meat, nuts, grains, eggs, seafood, cheese or vegetarian sources like soy. These diets often restrict carbs like cereals, grains, fruits, and possibly vegetables.'
Label(frame, text=text, wraplength=350, font="helvetica 14").grid(row=0, column=2, sticky=W)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
frame.bind("<Configure>", on_configure)

root.mainloop()
