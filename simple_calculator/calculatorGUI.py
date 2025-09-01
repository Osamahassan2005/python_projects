import tkinter
from tkinter import Tk, Button, Entry, StringVar, Frame, Image

# Initialize the main window
r = Tk()
r.geometry('370x570')
r.title('CALCULATOR')

# Function for button click
def click(event):
    global svalue
    text = event.widget.cget('text')
    if text == 'C':
        svalue.set('0')
    elif text == '=':
        try:
            svalue.set(eval(svalue.get()))
        except :
            svalue.set("Error")
    else:
        if svalue.get() == '0':
            svalue.set(text)
        else:
            svalue.set(svalue.get() + text)

# Variable for entry field
svalue = StringVar(value='0')

# Entry widget
e = Entry(r, textvariable=svalue, font='lucida 20 italic', borderwidth=5, relief='ridge')
e.pack(pady=10,ipady=20,fill='x', padx=10)

# Main container frame for all buttons
mf = Frame(r, bg='grey')
mf.pack()

# Frame for number buttons (1-9) and 0, =, C
fn = Frame(mf, bg='grey')
fn.grid(row=0, column=0)

# Add number buttons (1-9)
x = 1
for i in range(3):
    fr = Frame(fn, bg='grey')
    fr.pack()
    for j in range(3):
        b = Button(fr, text=str(x), padx=20, pady=20, font='lucida 20 bold', relief='raised')
        b.pack(side='left', padx=5, pady=5)
        b.bind('<Button-1>', click)
        x += 1

# Add 0, =, C buttons -framebottom
fb= Frame(fn, bg='grey')
fb.pack()
for i in ['0', '=', 'C']:
    b = Button(fb, text=i, padx=20, pady=20, font='lucida 20 bold', relief='raised')
    b.pack(side='left', padx=5, pady=5)
    b.bind('<Button-1>', click)

# Frame for operation buttons (+, -, *, /)
fo = Frame(mf, bg='grey')
fo.grid(row=0, column=1, sticky='ns')  # Right side, vertically aligned

for i in ['+', '-', '*', '/']:
    b = Button(fo, text=i, padx=20, pady=18, font='lucida 20 bold', relief='raised')
    b.pack(pady=9)
    b.bind('<Button-1>', click)

# Run the main loop
r.mainloop()
