import re
errmsg = StringVar()
formatmsg = "Zip should be ##### or #####-####"


# Called when the user types in the entry field, or when the field loses focus.
def check_zip(newval, op):
    errmsg.set('')
    valid = re.match('^[0-9]{5}(\-[0-9]{4})?$', newval) is not None
    btn.state(['!disabled'] if valid else ['disabled'])
    if op=='key':
        ok_so_far = re.match('^[0-9\-]*$', newval) is not None and len(newval) <= 10
        if not ok_so_far:
            errmsg.set(formatmsg)
        return ok_so_far
    elif op=='focusout':
        if not valid:
            errmsg.set(formatmsg)
    return valid
check_zip_wrapper = (root.register(check_zip), '%P', '%V')

zip = StringVar() # The zip code entered by the user
f = ttk.Frame(root) # The outer frame
f.grid(column=0, row=0) # Grid the outer frame
ttk.Label(f, text='Name:').grid(column=0, row=0, padx=5, pady=5) # Grid a label 
ttk.Entry(f).grid(column=1, row=0, padx=5, pady=5) # Grid an entry widget
ttk.Label(f, text='Zip:').grid(column=0, row=1, padx=5, pady=5) # Grid a label
e = ttk.Entry(f, textvariable=zip, validate='all', validatecommand=check_zip_wrapper) # Grid an entry widget
e.grid(column=1, row=1, padx=5, pady=5) # Grid an entry widget
btn = ttk.Button(f, text="Process") # Create a button
btn.grid(column=2, row=1, padx=5, pady=5) # Grid the button
btn.state(['disabled']) # Disable the button
msg = ttk.Label(f, font='TkSmallCaptionFont', foreground='red', textvariable=errmsg) # Create a label
msg.grid(column=1, row=2, padx=5, pady=5, sticky='w') # Grid the label