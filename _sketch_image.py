from tkinter import*
from tkinter import Tk, ttk

from PIL import Image, ImageTk
from tkinter import filedialog as fd
import cv2

co0 = "#ffffff"
co1 = "#000000"
co2 = "#63b9ff"

window = Tk()
window.title("Image")
window.geometry('300x436')
window.configure(background=co0)
window.resizable(width=False, height=False)

global original_img, l_img, img
original_img = ['']


def choose_img():
    global original_img, l_img, img
    img = fd.askopenfilename()
    original_img.append(img)

    img = Image.open(img)
    img = img.resize((160, 200))
    img = ImageTk.PhotoImage(img)

    l_img = Label(window, image=img, bg=co0, fg=co1)
    l_img.place(x=70, y=60)


def convert_img():
    global original_img, l_img, img
    scale_value = scale.get()
    img = cv2.imread(original_img[-1])
    converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(converted_img, (25, 25), 300, 300)
    img_to_pencil = cv2.divide(converted_img, blurred_img, scale=scale_value)
    cv2.imwrite("saved_img.png", img_to_pencil)

    img = Image.open("saved_img.png")
    img = img.resize((160, 200))
    img = ImageTk.PhotoImage(img)

    l_img = Label(window, image=img, bg=co0, fg=co1)
    l_img.place(x=70, y=60)


def convert_image():
    global original_img, l_img, img
    scale_value = scale.get()
    img = cv2.imread(original_img[-1])
    converted_img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    blurred_img = cv2.GaussianBlur(converted_img, (21, 21), 0)
    img_to_pencil = cv2.divide(converted_img, blurred_img, scale=scale_value)
    cv2.imwrite("saved_img.png", img_to_pencil)

    img = Image.open("saved_img.png")
    img = img.resize((160, 200))
    img = ImageTk.PhotoImage(img)

    l_img = Label(window, image=img, bg=co0, fg=co1)
    l_img.place(x=70, y=60)


def convert_bw():
    global original_img, l_img, img
    scale_value = scale.get()
    img = cv2.imread(original_img[-1])
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("bw_ig.png", gray_img)
    img = Image.open("bw_ig.png")
    img = img.resize((160, 200))
    img = ImageTk.PhotoImage(img)

    l_img = Label(window, image=img, bg=co0, fg=co1)
    l_img.place(x=70, y=60)


style = ttk.Style(window)
style.theme_use("clam")

app_img = Image.open("face.ico")
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(window, image=app_img, text="Image To Sketch", width=300, compound=LEFT, relief=RAISED, anchor=NW, font=('System 15 bold'), bg=co0, fg=co1)
app_logo.place(x=0, y=0)

l_option = Label(window, text="settings.............................................................................".upper(), anchor=NW, font=('verdana 10 bold'), bg=co0, fg=co1)
l_option.place(x=10, y=260)

scale = Scale(window, from_=0, to=255, length=120, bg=co0, fg='red', orient=HORIZONTAL)
scale.place(x=10, y=287)

b_choose = Button(window, text="Choose img", command=choose_img, width=15, overrelief=RIDGE, font=('Ivy 10'), bg=co2, fg=co1)
b_choose.place(x=147, y=287)

b_pen = Button(window, text="Black&White", command=convert_bw, width=15, overrelief=RIDGE, font=('Ivy 10'), bg=co2, fg=co1)
b_pen.place(x=147, y=317)

b_blue = Button(window, text="Pencil Sketch", command=convert_image, width=15, overrelief=RIDGE, font=('Ivy 10'), bg=co2, fg=co1)
b_blue.place(x=147, y=347)

b_sketch = Button(window, text="Pen Sketch", command=convert_img, width=15, overrelief=RIDGE, font=('Ivy 10'), bg=co2, fg=co1)
b_sketch.place(x=147, y=377)

window.mainloop()









