from tkinter import *


# this will convert kg to pounds, ounces and grams.
# it will use a tkinter interface.

window=Tk() # create the window

# set up the functions


def kg_to_pound():
    print(e1_value.get()) #print whatever's in e1
    pounds=e1_value.get()*2.20462 # convert to pounds
    t1.insert(END,pounds) # in t1, insert that amount

# ================
# conversions:
# 1 kg = 1000 grams
# 1 kg = 2.20462 pounds
# 1 kg = 35.274 ounces
# ==================
e1_value=StringVar()

# set up a 3 column (w) by 2 column (tall)

# define buttons
b1 = Button(window,textvariable=e1_value)
    # grid
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)



window.mainloop() #required for all windows to draw
