from tkinter import * # Import tkinter 
from tkinter import ttk # Import ttk (Themed Tk)

root = Tk() # Create a window 

l =ttk.Label(root, text="Starting...") # Create a label

l.grid() # Place the label in the window
l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside')) # Bind the mouse enter event to the label
l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside')) # Bind the mouse leave event to the label
l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button')) # Bind the mouse button press event to the label
l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button')) # Bind the mouse button press event to the label
l.bind('<Double-1>', lambda e: l.configure(text='Double clicked')) # Bind the mouse double click event to the label
l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y))) # Bind the mouse button drag event to the label
root.mainloop() # Start the main loop