from ctypes import pointer
from curses import window
from tkinter import *
import turtle
from PIL import ImageTk, Image
import pyautogui as pag
import sys

sys.setrecursionlimit(3000)

tkFenster = Tk()
last_position = (0, 0)
tkFenster.geometry("830x700")
previous_pointer_position = (0, 0)
canv = Canvas(master=tkFenster, highlightthickness=2, highlightbackground="black")
mouse_pointer = turtle.RawTurtle(canv)
mouse_pointer.penup()
mouse_pointer.setposition(200, -10)
def select_color():
    color = click.get()
    mouse_pointer.color(color)
colors = ["black", "red", "green", "blue", "orange", "purple", "voilet", "pink"]
click = StringVar()
click.set("black")
color_dropdown = OptionMenu(tkFenster, click, *colors)
color_select_btn = Button(tkFenster, text="Select", command=select_color)
# mouse_pointer.setheading(75)
# mouse_pointer.hideturtle()

def motion(event):
    global previous_pointer_position
    x, y = event.x, event.y
    x = x - 240
    y = 165 - y
    if last_position != (x, y):
        mouse_pointer.setposition(x, y)
    if previous_pointer_position != (x, y):
        mouse_pointer.pendown()
        mouse_pointer.setposition(x, y)
        mouse_pointer.penup()
        previous_pointer_position = (x, y)

canv.place(x=15, y=20, width=800, height=400)

color_dropdown.place(x=15, y=440, width=150, height=30)
color_select_btn.place(x=180, y=440, width=150, height=30)
# canv.
# img = ImageTk.PhotoImage(Image.open("C:\\Users\\msi 1\\Python Projects\\oneTimeProjects\\assignment\\2048\\download.jpg").resize((400, 300)))

# canv.create_image(0, 0, image=img, anchor='nw')
canv.bind("<B1-Motion>", motion)
# color_select_btn.bind("Button-1", select_color)
mainloop()
