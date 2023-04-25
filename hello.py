# Description: Hello World in Tkinter
from tkinter import *
from tkinter import ttk

# Create a window
root = Tk()
# Set the title of the window
ttk.Button(root, text="Hello World").grid()
# Start the main loop
root.mainloop()