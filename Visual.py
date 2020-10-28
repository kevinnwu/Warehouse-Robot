from __future__ import print_function
from ortools.linear_solver import pywraplp

from tkinter import *
# from PIL import ImageTk, Image
import sqlite3

# function to create bot
def create_bot(x, y):
    return canvas.create_oval(x*20, 600-(y*20), (x+1)*20, 600-((y+1)*20), fill='green')

# function to create place
def create_place(x, y):
    return canvas.create_rectangle(x*20, 600-(y*20), (x+1)*20, 600-((y+1)*20), fill='green')
z = 0
x =0
def show():
    global z
    z = z + 1
    label = Label(frame, text=clicked.get()).grid(row=z, column=1)


root = Tk()
root.geometry("1000x700")

# canvas
canvas = Canvas(root, width=600, height=600, bg="white")
canvas.grid(row=0, column=0, rowspan=2)
# create grid
for i in range(1, 30):
    canvas.create_line(0, i*20, 800, i*20, fill='Grey')
    canvas.create_line(i*20, 0, i*20, 800, fill='Grey')
# create box
create_place(1, 2)
create_place(6, 8)
# create oval
create_bot(0, 0)

frame = LabelFrame(root, text='order', padx=100, pady=200)
frame.grid(row=0, column=1)

add_button = Button(frame, text='submit', padx=40, pady=20, command=show)
add_button.grid(row=0, column=4)

options =[
    'Monday',
    'Tuesday',
    'Wednesday'
]
clicked = StringVar()
clicked.set('test')
drop = OptionMenu(frame, clicked, *options)
drop.grid(row=0, column=1)

conn = sqlite3.connect('Warehouse_Robot')

root.mainloop()
