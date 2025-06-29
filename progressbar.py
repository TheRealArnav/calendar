from tkinter.ttk import*
from tkinter import*
import time


root = Tk()
progress_bar = Progressbar(root, orient = 'horizontal', length = 100, mode = "indeterminate")

def bar():
    progress_bar["value"] = 20
    root.update_idletasks()
    time.sleep(1)
    progress_bar["value"] = 40
    root.update_idletasks()
    time.sleep(1)
    progress_bar["value"] = 60
    root.update_idletasks()
    time.sleep(1)
    progress_bar["value"] = 80
    root.update_idletasks()
    time.sleep(1)
    progress_bar["value"] = 100
    root.update_idletasks()
    time.sleep(1)
    


btn = Button(root, text = "Start", background = "grey", command = bar)


progress_bar.pack()
btn.pack(side = "bottom")







root.mainloop()