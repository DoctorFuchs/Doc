from tkinter import *
from sys import *
from config import *

root = Tk()

#make screen to fullscreen
if platform != "linux":
    root.attributes("-fullscreen", True)

else:
    root.attributes("-zoomed", True)

root.title("DOC")

#screenformat
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

screenHeightinMM = root.winfo_screenmmheight()
screenWidthinMM = root.winfo_screenmmwidth()

addx = screenWidth / 800
addy = screenHeight / 800

#fonts
x = (111/(508/screenHeightinMM))*addy
smallT = int(x/13.3)
normalT = int(x/5)
codeT = int(x/6.6)
title5T = int(x/5)
titleT = int(x)

small = f"Calibri {smallT}"
normal = f"Calibri {normalT}"
code = ("Source Code Pro", codeT)
title5 = f"Calibri {title5T} bold"
title = f"Calibri {titleT} bold underline"

#make Canvas at root
c = Canvas(root, width=screenWidth, height=screenHeight, bg='white')

def between(eventx, eventy, x1, y1, x2, y2):
    if x1 <= eventx <= x2:
        if y1 <= eventy <= y2:
            return True

        else:
            return False
    else:
        return False

class create_boxes:
    def __init__(self):
        self.dark = False

    def all(self, dark_mode=False):
        self.dark=dark_mode
        self.box1(high=dark_mode)
        self.box2(high=dark_mode)
        self.box3(high=dark_mode)
        self.box4(high=dark_mode)
        self.box5(high=dark_mode)
        self.box6(high=dark_mode)
        self.box7(high=dark_mode)
        self.box8(high=dark_mode)

        if not dark_mode:
            c.create_line(0*addx, 50*addy, 800*addx, 50*addy)

    def box1(self, high=False):
        if not high:
            c.create_rectangle(0*addx, 0*addy, 100*addx, 50*addy, fill='white', outline="white")
            c.create_text(20*addx, 25*addy, anchor='w', fill='black', font=title5+" underline", text=box1)

        else:
            c.create_rectangle(0*addx, 0*addy, 100*addx, 50*addy, fill='black')
            c.create_text(20*addx, 25*addy, anchor='w', fill='white', font=title5+" underline", text=box1)

    def box1Action(self):
        pass

    def box2(self, high=False):
        if not high:
            c.create_rectangle(100*addx, 0*addy, 200*addx, 50*addy, fill='white', outline="white")
            c.create_text(20*addx, 25*addy, anchor='center', fill='black', font=title5+" underline", text=box2)
        else:
            c.create_rectangle(100*addx, 0*addy, 200*addx, 50*addy, fill='black')
            c.create_text(20*addx, 25*addy, anchor='center', fill='white', font=title5+" underline", text=box2)

    def box2Action(self):
        pass

    def box3(self, high=False):
        if not high:
            c.create_rectangle(200*addx, 0*addy, 300*addx, 50*addy, fill='white', outline="white")
            c.create_text(20*addx, 25*addy, anchor='center', fill='black', font=title5+" underline", text=box3)
        else:
            c.create_rectangle(200*addx, 0*addy, 300*addx, 50*addy, fill='black')
            c.create_text(20*addx, 25*addy, anchor='center', fill='white', font=title5+" underline", text=box3)

    def box3Action(self):
        pass

    def box4(self, high=False):
        if not high:
            c.create_rectangle(300*addx, 0*addy, 400*addx, 50*addy, fill='white', outline="white")
            c.create_text(20*addx, 25*addy, anchor='center', fill='black', font=title5+" underline", text=box4)
        else:
            c.create_rectangle(300*addx, 0*addy, 400*addx, 50*addy, fill='black')
            c.create_text(20*addx, 25*addy, anchor='center', fill='white', font=title5+" underline", text=box4)

    def box4Action(self):
        pass

    def box5(self, high=False):
        if not high:
            c.create_rectangle(400*addx, 0*addy, 500*addx, 50*addy, fill='white', outline="white")
            c.create_text(20*addx, 25*addy, anchor='center', fill='black', font=title5+" underline", text=box5)
        else:
            c.create_rectangle(400*addx, 0*addy, 500*addx, 50*addy, fill='black')
            c.create_text(20*addx, 25*addy, anchor='center', fill='white', font=title5+" underline", text=box5)

    def box5Action(self):
        pass

    def box6(self, high=False):
        if not high:
            c.create_rectangle(500*addx, 0*addy, 600*addx, 50*addy, fill='white', outline="white")
            c.create_text(20*addx, 25*addy, anchor='center', fill='black', font=title5+" underline", text=box6)

        else:
            c.create_rectangle(500*addx, 0*addy, 600*addx, 50*addy, fill='black')
            c.create_text(20*addx, 25*addy, anchor='center', fill='white', font=title5+" underline", text=box6)

    def box6Action(self):
        pass

    def box7(self, high=False):
        if not high:
            c.create_rectangle(600*addx, 0*addy, 700*addx, 50*addy, fill='white', outline="white")
            c.create_text(20*addx, 25*addy, anchor='center', fill='black', font=title5+" underline", text=box7)
        else:
            c.create_rectangle(600*addx, 0*addy, 700*addx, 50*addy, fill='black')
            c.create_text(20*addx, 25*addy, anchor='center', fill='white', font=title5+" underline", text=box7)

    def box7Action(self):
        pass

    def box8(self, high=False):
        if not high:
            c.create_rectangle(700*addx, 0*addy, 800*addx, 50*addy, fill='white', outline="white")
            c.create_text(20*addx, 25*addy, anchor='center', fill='black', font=title5+" underline", text=box8)
        else:
            c.create_rectangle(700*addx, 0*addy, 800*addx, 50*addy, fill='black')
            c.create_text(20*addx, 25*addy, anchor='center', fill='white', font=title5+" underline", text=box8)

    def box8Action(self):
        pass

    def motion(self, event):
        if between(event.x, event.y, 0, 0, 800*addx, 50*addy):
            pass



#init
boxes = create_boxes()

#start
boxes.all(dark_mode=False)

#pack and mainloop
c.pack()

root.mainloop()