#normal woekout

from tkinter import *
from PIL import Image, ImageTk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()
root.title('WORKOUT ROUTINE')
root.geometry('1300x700')

canvas = Canvas(root, )
canvas.pack(side=LEFT, fill=BOTH, expand=True)
frame = Frame(canvas, )
canvas.create_window((0, 0), window=frame, anchor='nw')
img1 = Image.open('suryanamaskar.png')
img1 = img1.resize((920, 650))
img1 = ImageTk.PhotoImage(img1)
imageLabel = Label(frame, image=img1)
imageLabel.grid(row=0, column=0, sticky=W)

scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
frame.bind("<Configure>", on_configure)

root.mainloop()
