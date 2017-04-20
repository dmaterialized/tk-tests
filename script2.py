from tkinter import *


# this will convert kg to pounds, ounces and grams.
# it will use a tkinter interface.

window=Tk() # create the window

# set up the functions

# ================
# conversions:
# 1 kg = 1000 grams
# 1 kg = 2.20462 pounds
# 1 kg = 35.274 ounces
# ==================


# convert to pounds
def kg_to_pound():
    print(e1_value.get()) # print whatever's in e1
    pounds=float(e1_value.get())*2.20462 # convert to pounds
    t1.insert(END,pounds) # in t1, insert that amount

# convert to ounces
# ...
# convert to grams
# ...

e1_value=StringVar()

# set up a 3 column (w) by 2 column (tall)

# define buttons
b1 = Button(window,textvariable=e1_value)
b1.pack() #(why is this needed?)
b1.grid(row=0,column=0) #place button here

#e1 is an input of text that stores in Entry ()
e1 = Entry(window,textvariable=e1_value)
# e1.pack() isn't needed for non-buttons
e1.grid(row=0,column=1)

# t1 is going to record values
t1=Text(window,height=1,width=10) # t1 is a text area on the right side
t1.grid(row=1,column=0)



window.mainloop() #required for all windows to draw
