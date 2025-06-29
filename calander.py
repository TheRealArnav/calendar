from tkinter import*
import calendar

root = Tk()
root.geometry("400x285")
root.title("Calander")





def Calender():
    calender_window = Tk()
    calender_window.geometry("500x600")
    calender_window.title("Caldender")
    calender_window.config(background = "light grey")
    year = int(entry.get())
    cal_info = calendar.calendar(year)
    label = Label(calender_window, text = cal_info, font = "Calibri 10")
    label.place(x = 20, y = 20)
    calender_window.mainloop()










root.config(background = "light grey")


label = Label(root, text = "CALANDER", background = "grey", width = 40, height = 5)

label.place(x = 70,y = 50)


label1 = Label(root, text = "ENTER YEAR", background = "light green", width = 10,height = 4)
label1.place(x = 175, y = 130)

entry = Entry(root, width = 10)
entry.place(x = 180, y = 200)

button = Button(root, text = "GENERATE CALANDER", background = "red", fg = "black", command = Calender)
button.place(x = 145,y = 230)

btn = Button(root, text = "EXIT", background = "red", fg = "black", command = root.destroy )
btn.place(x = 195, y = 260)







root.mainloop()