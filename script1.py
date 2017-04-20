from tkinter import *

window=Tk()

# set up the functions
def km_to_miles():
    print(e1_value.get()) # value.get() lets us pull a value from Entry.
    # insert a value to the text widget
    miles=float(e1.value.get())*1.606 # didn't need to add float here, why not?
    t1.insert(END,miles) # end enters new text at the end of any existing text.

b1 = Button(window,text="String Execute", command=km_to_miles)
#  first, tell the button which window it's backed to.
#  then, tell the text that should be used.
#  command links it to a function.
b1.pack() # apparently needed in order to create the button
b1.grid(row=0,column=0) #

# grid is supposed to be better because you specify row/column.
# we want a 2x5 grid layout.
#
# step 2 was to add line below:
e1_value=StringVar() # this is to hold the string and be able to use get methods on it
e1 = Entry(window,textvariable=e1_value) # --> textvariable=e1_value
# create new button, specify window, don't specify label as it's a text area.
e1.grid(row=0,column=1) # # place the button at these coords


# instance a text item; height is 1 row tall
t1=Text(window,height=1,width=20) # t1 is a text area
t1.grid(row=0,column=2) #t1 is at these coords

# ... ... ...
window.mainloop() # required for all windows to draw.
