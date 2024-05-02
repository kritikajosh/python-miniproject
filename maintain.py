#maintain weight
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
img1 = Image.open('maintain.png')
img1 = img1.resize((920, 650))
img1 = ImageTk.PhotoImage(img1)
imageLabel = Label(frame, image=img1)
imageLabel.grid(row=0, column=0, sticky=W)

text="An eating plan that helps promote health and manage your weight includes a variety of healthy foods. Add an array of colors to your plate and think of it as eating the rainbow. Dark, leafy greens, oranges, and tomatoes—even fresh herbs—are loaded with vitamins, fiber, and minerals. Adding frozen peppers, broccoli, or onions to stews and omelets gives them a quick and convenient boost of color and nutrients.An eating plan that helps promote health and manage your weight includes a variety of healthy foods. Add an array of colors to your plate and think of it as eating the rainbow. Dark, leafy greens, oranges, and tomatoes—even fresh herbs—are loaded with vitamins, fiber, and minerals. Adding frozen peppers, broccoli, or onions to stews and omelets gives them a quick and convenient boost of color and nutrients."
Label(frame, text=text, wraplength=350, font="helvetica 14").grid(row=0, column=2, sticky=W)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
frame.bind("<Configure>", on_configure)

root.mainloop()
