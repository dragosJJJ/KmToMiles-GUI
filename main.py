from tkinter import *

FONT = ("Courier",12)

window = Tk()
window.title("Convert")
window.minsize(width=200,height=100)


input = Entry(window, width=12)
input.grid(row=0, column=1)


label1 = Label(window, text="Km", font=FONT)
label2 = Label(window, text="is equal to", font= FONT)
label3 = Label(window, text="Miles", font=FONT)

label1.grid(row=0, column=2)
label2.grid(row=1, column=0)
label3.grid(row=1, column=2)

text = Text(font=FONT, height= 1, width=12)
text.grid(row=1,column=1)

def calc():
    miles =  round(0.621371 * float(input.get()))
    text.delete(1.0, END)
    text.insert(END, str(miles))

button = Button(window, text="Calculate", command=calc)
button.grid(row=2, column=1)

window.mainloop()