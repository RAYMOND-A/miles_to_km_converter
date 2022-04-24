from tkinter import *

windows = Tk()
windows.minsize(width=500, height=300)
windows.title("Miles to Kilometer converter")
windows.config(padx=20, pady=20)

def miles_to_km():
    miles = float(input_entry.get())
    km = miles*1.609
    km_result_label.config(text=f"{km}")

input_entry = Entry(width=8)
print(input_entry.get())
input_entry.grid(row=2, column=2)


miles_label = Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(row=2, column=3)

is_equal_label = Label(text="is equal to", font=("Arial", 20, "bold"))
is_equal_label.grid(row=3, column=0)

km_result_label = Label(text="0", font=("Arial", 20, "bold"))
km_result_label.grid(row=3, column=2)

km_label = Label(text="KM", font=("Arial", 20, "bold"))
km_label.grid(row=3, column=3)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=4, column=2)


windows.mainloop()