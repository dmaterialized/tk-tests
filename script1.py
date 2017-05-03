# \ button to convert km unit to miles
# / v: 1.0
# \
# /
# \
# /
# \
from tkinter import * # all funcs

# ==== i n i t   w i n d o w =============================
window=Tk() # init tkinter window

# set up the functions
def km_to_miles():
    print(float(e1_value.get())) # testing purposes only


    # 1. value.get() lets us pull a value from Entry.
    # 2. insert a value to the text widget
    # 3. # END enters new text into a text area, but at the end of any existing text.
    miles = float(e1_value.get())*1.6
#   ^^ ||| the trouble spot ||| ^^
#          edit: was referencing e1.value, not e1_value.
#          lesson learned.
    t1.insert(END,miles)

b1 = Button(window,text="String Execute",command=km_to_miles)
#  first, tell the button which window it's backed to.
#  then, tell the text that should be used.
#  command links it to a function.
b1.pack() # this is apparently needed in order to create the button
b1.grid(row=0,column=0) # place the button in the upper-left corner.

# grid is supposed to be better because you specify row/column.
# we want a 2x5 grid layout.
#
# step 2 was to add line below:
e1_value = StringVar() # this is to hold the string and be able to use get methods on it
e1 = Entry(window,textvariable=e1_value) # --> textvariable=e1_value
# create new button, specify window, don't specify label as it's a text area.
e1.grid(row=0,column=1) # # place the button at these coords


# instance a text item; height is 1 row tall
t1=Text(window,height=1,width=20) # t1 is a text area
t1.grid(row=0,column=2) #t1 is at these coords (line one, right-side column)

# ... ... ...
window.mainloop() # required for all windows to draw.
# ========================================================
#   w i n d o w   1   e n d s
