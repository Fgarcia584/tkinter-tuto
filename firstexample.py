from tkinter import * # Import tkinter
from tkinter import ttk # Import ttk (Themed Tk)

# This is the function that will be called when the button is clicked
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk() # Create a window
root.title("Feet to Meters") # Set the title of the window

mainframe = ttk.Frame(root, padding="3 3 12 12") # Create a frame with padding 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # Place the frame in the window
root.columnconfigure(0, weight=1) # Configure the column to be resized
root.rowconfigure(0, weight=1) # Configure the row to be resized

feet = StringVar() # Create a string variable
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) # Create an entry widget
feet_entry.grid(column=2, row=1, sticky=(W, E)) # Place the entry widget in the frame

meters = StringVar() # Create a string variable
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E)) # Create a label and place it in the frame

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W) # Create a button and place it in the frame

# Create labels for the entry widgets
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W) 
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# Create a menu
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)


# Bind the enter key to the calculate function
feet_entry.focus()
root.bind("<Return>", calculate)

# Start the main loop
root.mainloop()