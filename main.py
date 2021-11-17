from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
window.config(padx=20, pady=20)


def convert():
    miles = float(input.get())
    km = round(miles * 1.609)
    display_label.config(text=f"{km}")


# Entry
input = Entry(width=7)
input.grid(column=1, row=0)
# Labels
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)
equal_label = Label(text="is equal to")
equale_label.grid(column=0, row=1)
display_label = Label(text="0")
display_label.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
# button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)
window.mainloop()
