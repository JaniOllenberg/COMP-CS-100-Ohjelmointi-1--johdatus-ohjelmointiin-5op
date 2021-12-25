from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()

#window stays on top of everything
root.wm_attributes("-topmost", 1)
root.update_idletasks()
# root.overrideredirect(True)
new = Tk()
new.wm_attributes("-topmost", 1)
new.update_idletasks()
new.overrideredirect(True)
new.mainloop()

root.mainloop()
