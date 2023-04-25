# Description: Menu
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
ttk.Entry(root).grid()
m = Menu(root) # Create a menu
m_edit = Menu(m) # Create a submenu
m.add_cascade(menu=m_edit, label="Edit") # Add the submenu to the menu
# Add commands to the submenu
m_edit.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>")) 
m_edit.add_command(label="Find...", command=lambda: root.event_generate("<<OpenFindDialog>>")) 
# Add a separator
root['menu'] = m

# Create a function to be called when the find command is selected
def launchFindDialog(*args):
    messagebox.showinfo(message="I hope you find what you're looking for!")
    
root.bind("<<OpenFindDialog>>", launchFindDialog) # Bind the find command to the function
# Start the main loop
root.mainloop()