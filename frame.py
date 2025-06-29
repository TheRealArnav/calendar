from tkinter import*


root = Tk()
root.geometry("400x400")
root.title("Frames")

heading = Label(root, text = "Types of sports", font = "Calibri 30")
heading.pack(side = "top")

frame1 = Frame(root,background = "grey")
frame1.pack(side = "left")

basketball = Button(frame1, text = "Basketball", fg = "Black", background = "white")
basketball.pack()

Volleyball = Button(frame1, text = "Volleyball", fg = "Black", bg = "white")
Volleyball.pack()

Karate = Button(frame1, text = "Karate", fg = "black", bg = "White")
Karate.pack()



frame2 = Frame(root,background = "Black")
frame2.pack(side = "right")

Tennis = Button(frame2, text = "Tennis", bg = "White", fg = "black")
Tennis.pack()

Cricket = Button(frame2, text = "Cricket", bg = "White", fg = "Black")
Cricket.pack()

Badminton = Button(frame2, text = "Badminton", bg = "White", fg = "black")
Badminton.pack()





root.mainloop()