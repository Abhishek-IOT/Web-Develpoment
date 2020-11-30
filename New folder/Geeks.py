import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

root=tk.Tk()
root.geometry("200x200")
img=ImageTk.PhotoImage(Image.open("photo1.jpg"))
img2=ImageTk.PhotoImage(Image.open("photo2.jpg"))
img3=ImageTk.PhotoImage(Image.open("photo4.jpg"))
l=Label()
l.pack()

x=1
def move():
    global x
    if x==4:
        x=1
    if x==1:
        l.config(image=img)
    elif x==2:
        l.config(image=img2)
    elif x==3:
        l.config(image=img3)
    x=x+1
    root.after(2000,move)
move()
root.mainloop()
