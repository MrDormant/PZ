import tkinter as tk
from tkinter import ttk


def reverse_number():
    n = entry_digit.get()
    result = int(str(n)[::-1])
    result_label.config(text=str(result))


app = tk.Tk()
app.title("Рассчитать в обратном порядке")

frame = ttk.Frame(app, padding="10 10 10 10")
frame.grid(row=0, column=0)

label_digit = tk.Label(frame, text="Введите трехзначное число:")
label_digit.grid(row=0, column=0, sticky=tk.W, pady=2)
entry_digit = tk.Entry(frame)
entry_digit.grid(row=0, column=1, pady=2)

calculate_button = ttk.Button(frame, text="Рассчитать", command=reverse_number)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=2)

app.mainloop()