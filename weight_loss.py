
from tkinter import *
from PIL import Image, ImageTk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

root = Tk()
root.title('DIET PLANS')
root.geometry('1300x700')

canvas = Canvas(root, bg="blue")
canvas.pack(side=LEFT, fill=BOTH, expand=True)
frame = Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame, anchor='nw')
img1 = Image.open('loss diet.png')
img1 = img1.resize((920, 650))
img1 = ImageTk.PhotoImage(img1)
imageLabel = Label(frame, image=img1)
imageLabel.grid(row=0, column=0, sticky=W)

text = "This gym meal plan aids weight loss by promoting a calorie deficit and ensuring sufficient protein intake for muscle preservation. Benefits include enhanced energy levels, improved exercise performance, and optimized recovery. A gym diet plan is crucial for achieving fitness objectives, as it provides the necessary fuel for workouts while facilitating fat loss and muscle development. Following an Indian gym diet plan helps to cultivate discipline, encourages mindful eating, and contributes to overall well-being, making it an essential component for individuals committed to maximizing their gym efforts and attaining sustainable fitness results."
Label(frame, text=text, wraplength=350, font="helvetica 14").grid(row=0, column=2, sticky=W)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=scrollbar.set)
frame.bind("<Configure>", on_configure)

root.mainloop()
