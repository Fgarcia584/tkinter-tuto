# Description: Grid geometry manager
from tkinter import *
from tkinter import ttk

root = Tk() # Create a window

content = ttk.Frame(root, padding=(3,3,12,12)) # Create a frame with padding
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100) # Create a frame with a border
namelbl = ttk.Label(content, text="Name") # Create a label
name = ttk.Entry(content) # Create an entry widget

# Create three checkbuttons
onevar = BooleanVar() 
twovar = BooleanVar()
threevar = BooleanVar()

# Set the initial values of the variables
onevar.set(True)
twovar.set(False)
threevar.set(True)


# Create the checkbuttons
one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True) # onvalue is the value to set the variable to when the checkbutton is checked
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True) # offvalue is the value to set the variable to when the checkbutton is unchecked
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True) # If offvalue is not specified, the variable is set to False
ok = ttk.Button(content, text="Okay") # Create a button
cancel = ttk.Button(content, text="Cancel") # Create a button

content.grid(column=0, row=0, sticky=(N, S, E, W)) # Place the frame in the window
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W)) # Place the frame in the window
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5) # Place the label in the window
name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5) # Place the entry widget in the window
one.grid(column=0, row=3) # Place the checkbutton in the window
two.grid(column=1, row=3) # Place the checkbutton in the window
three.grid(column=2, row=3) # Place the checkbutton in the window
ok.grid(column=3, row=3) # Place the button in the window
cancel.grid(column=4, row=3) # Place the button in the window

root.columnconfigure(0, weight=1) # Configure the column to be resized
root.rowconfigure(0, weight=1) # Configure the row to be resized
content.columnconfigure(0, weight=3) # Configure the column to be resized
content.columnconfigure(1, weight=3) # Configure the column to be resized
content.columnconfigure(2, weight=3) # Configure the column to be resized
content.columnconfigure(3, weight=1) # Configure the column to be resized
content.columnconfigure(4, weight=1) # Configure the column to be resized
content.rowconfigure(1, weight=1) # Configure the row to be resized

root.mainloop() # Start the main loop