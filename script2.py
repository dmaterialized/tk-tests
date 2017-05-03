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
    t1.insert(END,pounds) # in t1, insert that amount at the end

# convert to ounces
def kg_to_oz():
    print(e1_value.get()) # print what's in e1
    ozs=float(e1_value.get())*35.274
    t1.insert(END,ozs)

# convert to grams
def kg_to_grams():
    print(e1_value.get()) #print what's in e1
    grams=float(e1_value.get())*1000
    t1.insert(END,grams)


def convert_from_kg():
    gram=float(e1_value.get())*1000
    pound=float(e1_value.get())*2.20462
    ounce=float(e1_value.get())*35.274
    t1.insert(END,gram)
    t2.insert(END,pound)
    t3.insert(END,ounce)

e1_value=StringVar()

# set up a 3 column (w) by 2 column (tall)
#
# define buttons
# use text not textvariable here!

b1 = Button(window,text="convert units",command=convert_from_kg)
#b1 = Button(window,text="convert to pounds",command=kg_to_pound)
b1.pack() # (why is this needed?)
b1.grid(row=0,column=0) # place button here

# b2=Button(window,text="convert to ounces",command=kg_to_oz)
# b2.pack()
# b2.grid(row=1,column=1)

# b3=Button(window,text="convert to grams",command=kg_to_grams)
# b3.pack()
# b3.grid(row=1,column=2)

# e1 is an input of text that stores in Entry ()
e1 = Entry(window,textvariable=e1_value)
# e1.pack() isn't needed for non-buttons
e1.grid(row=0,column=1)
# middle

# t1 is going to record values
t1=Text(window,height=1,width=10) # t1 is a text area on the right side
t1.grid(row=1,column=0)

# bottom middle
t2=Text(window,height=1,width=10)
t2.grid(row=1,column=1)

# bottom right
t3=Text(window,height=1,width=10)
t3.grid(row=1,column=2)

# how to set up a label?
# l1=Label("kg")
# l1.grid(row=0,column=1)
# apparently it's

l1=Label(window,text="Grams")
l1.grid(row=2,column=0)
#
l2=Label(window,text="Pounds")
l2.grid(row=2,column=1)
#
l3=Label(window,text="Ounces")
l3.grid(row=2,column=2)
#
l4=Label(window,text="kg")
l4.grid(row=0,column=2)
# TODO
# remains to be done:
# - convert to all three values automatically
# - layout is intended to be either
#   0       1       2
# 0  |"kg" | text | convert |
# 1  |val1  | val2  |  val3 |
# - or:
#       0       1       2
# 0  |convert | text | "kg" |
# 1  |  val1  | val2 | val3 |
#   |
#


window.mainloop() #required for all windows to draw
