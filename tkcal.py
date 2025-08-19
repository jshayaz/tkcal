# step 1: import tkinter
from tkinter import *

# step 2: gui interaction
window = Tk()

# step 3: writing inputs
window.geometry("300x400")
window.title("Python calculator")
e = Entry(window, width=35, borderwidth=5)
e.place(x=0, y=0)

# creating buttons
def click(n):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(n))

button = Button(window, text="1", width=12, command=lambda: click(1))
button.place(x=10, y=60)
button = Button(window, text="2", width=12, command=lambda: click(2))
button.place(x=80, y=60)
button = Button(window, text="3", width=12, command=lambda: click(3))
button.place(x=170, y=60)
button = Button(window, text="4", width=12, command=lambda: click(4))
button.place(x=10, y=120)
button = Button(window, text="5", width=12, command=lambda: click(5))
button.place(x=80, y=120)
button = Button(window, text="6", width=12, command=lambda: click(6))
button.place(x=170, y=120)
button = Button(window, text="7", width=12, command=lambda: click(7))
button.place(x=10, y=180)
button = Button(window, text="8", width=12, command=lambda: click(8))
button.place(x=80, y=180)
button = Button(window, text="9", width=12, command=lambda: click(9))
button.place(x=170, y=180)
button = Button(window, text="0", width=12, command=lambda: click(0))
button.place(x=10, y=240)

def add():
    try:
        n1 = float(e.get())
        global math
        math = "addition"
        global i
        i = n1
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid Input")

button = Button(window, text="+", width=12, command=add)
button.place(x=80, y=240)

def sub():
    try:
        n1 = float(e.get())
        global math
        math = "subtraction"
        global i
        i = n1
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid Input")

button = Button(window, text="-", width=12, command=sub)
button.place(x=170, y=240)

def mult():
    try:
        n1 = float(e.get())
        global math
        math = "multiplication"
        global i
        i = n1
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid Input")

button = Button(window, text="*", width=12, command=mult)
button.place(x=10, y=300)

def div():
    try:
        n1 = float(e.get())
        global math
        math = "division"
        global i
        i = n1
        e.delete(0, END)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid Input")

button = Button(window, text="/", width=12, command=div)
button.place(x=80, y=300)

def equal():
    try:
        n1 = float(e.get())
        e.delete(0, END)
        if math == "addition":
            e.insert(0, i + n1)
        elif math == "subtraction":
            e.insert(0, i - n1)
        elif math == "multiplication":
            e.insert(0, i * n1)
        elif math == "division":
            if n1 == 0:
                e.insert(0, "Error: Div by 0")
            else:
                e.insert(0, i / n1)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Invalid Input")

button = Button(window, text="=", width=12, command=equal)
button.place(x=170, y=300)

def clear():
    e.delete(0, END)

button = Button(window, text="clear", width=18, command=clear)
button.place(x=80, y=350)

# step 4: main loop
window.mainloop()
