from tkinter import*


root = Tk()

root.title("menu")

menu = Menu(root)

file = Menu(menu, tearoff = 0)
menu.add_cascade(label = "File", menu = file)
file.add_command(label = "New File", command = None)
file.add_command(label = "Open...", command = None)
file.add_command(label = "Save", command = None)
file.add_separator()
file.add_command(label = "Exit",command = None)

edit = Menu(menu,tearoff = 0)
menu.add_cascade(label = "Edit",menu = edit)

edit.add_command(label = "Cut",command = None)
edit.add_command(label = "Copy", command = None)
edit.add_command(label = "Paste",command = None)
edit.add_command(label = "select",command = None)
edit.add_separator()
edit.add_command(label = "Find...",command = None)
edit.add_command(label = "Find All", command  = None)

help = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Help", menu = help)

help.add_command(label = "Help", command = None)
help.add_command(label = "Demo", command = None )
help.add_separator()
help.add_command(label = "About Tk", command  = None)







root.config(menu = menu)






root.mainloop()