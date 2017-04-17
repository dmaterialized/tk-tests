from tkinter import *


# this will convert kg to pounds, ounces and grams.
# it will use a tkinter interface.

window=Tk() # create the window

# set up the functions

e1_value=stringVar()


def kg_to_pound():
    print(e1_value.get()) #print whatever's in weightinput
    pounds=e1_value.get()*2.20462
    t1.insert(END,pounds)

# ================
# conversions:
# 1 kg = 1000 grams
# 1 kg = 2.20462 pounds
# 1 kg = 35.274 ounces
# ==================


# set up a 3 column (w) by 2 column (tall)

# define buttons
b1 = Button(window,textvariable=e1_value)
    # grid
t1.grid(row=0,column=2)


window.mainloop() #required for all windows to draw
