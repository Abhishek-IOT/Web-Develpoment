from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Image Viewer")
root.geometry("208x228")
my_img4 = ImageTk.PhotoImage(Image.open("photo1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("photo2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open(("photo3.jpg")))
my_img1=ImageTk.PhotoImage(Image.open("photo4.jpg"))
imag_list = [my_img1, my_img2, my_img3,my_img4]

def back(img_no):
    global label
    global button_for
    global button_back
    label.grid_forget()
    label = Label(image=imag_list[img_no - 1])
    label.grid(row=1, column=0, columnspan=3)
    button_for = Button(root, text="forward", command=lambda: forward(img_no + 1))
    button_back = Button(root, text="Back", command=lambda: back(img_no -1))
  #  print(img_no)
    if img_no == 1:
        button_back = Button(root, Text="Back", state=DISABLED)
    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_for.grid(row=5, column=2)

def forward(img_no):
    global label
    global button_for
    global button_back
    label.grid_forget()
    label = Label(image=imag_list[img_no-1])
    label.grid(row=1, column=0, columnspan=3)
    button_for = Button(root, text="forward", command=lambda: forward(img_no+1))
    if img_no==4:
        button_for=Button(root,text="Forward",state=DISABLED)
    button_back=Button(root,text="Back",command=lambda :back(img_no-1))

    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1)
    button_for.grid(row=5, column=2)
   # print(img_no)

label = Label(image=my_img1)
label.grid(row=1, column=0, columnspan=3)
button_back=Button(root,text="Back",command=back,state=DISABLED)
button_exit = Button(root, text="exit",command=root.quit)
button_for = Button(root, text="Forward",command=lambda :forward(1))
button_back.grid(row=5,column=0)
button_exit.grid(row=5,column=1)
button_for.grid(row=5,column=2)
root.mainloop()
