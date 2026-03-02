from tkinter import *
from tkinter import ttk
import random

def get_param():
    a = float(a_entry.get())
    b = float(b_entry.get())
    size = int(n_entry.get())
    get_result(size, a, b)


def get_m(N):
    sum = 0
    for i in N:
        sum += i
    return sum / len(N)

def get_g(N, m):
    sum = 0
    for i in N:
        sum += (i**2)
    return (sum / len(N) - m**2)

def get_result(size, a, b):
    N = []

    for i in range(size):
        rand = random.random()
        N.append(a + rand * (b - a))

    MX = (a + b) / 2
    DX = ((a - b)**2) / 12

    m = get_m(N)
    g = get_g(N, m)
    d_1_label.configure(text= "Δ 1 = %.6f" % (abs(MX - m)), font='Courier 16')
    d_2_label.configure(text= "Δ 2 = %.6f" % (abs(DX - g)), font='Courier 16')
    numbers.delete("0.0", END)
    for i in range(5):
        for j in range(4):
            numbers.insert(END, "%.4f |\t" % (N[i+j]) if j < 3 else "%.4f\n" % (N[i+j]) if i < 4 else "%.4f" % (N[i+j]))

root = Tk()
root.title("Моделирование равномерного распределения")
Label(text = "a", font='Courier 16').grid(column=1, row=0)
a_entry = ttk.Entry(width=6, font='Courier 16')
a_entry.grid(column=1, row=1, padx=5)

Label(text = "b", font='Courier 16').grid(column=3, row=0)
b_entry = ttk.Entry(width=6, font='Courier 16')
b_entry.grid(column=3, row=1, padx=5)

Label(text = "N", font='Courier 16').grid(column=5, row=0)
n_entry = ttk.Entry(width=6, font='Courier 16')
n_entry.grid(column=5, row=1, padx=5)


d_1_label = Label(text = "Δ 1 = ", font='Courier 16')
d_1_label.grid(column=2, row=3)

d_2_label = Label(text = "Δ 2 = ", font='Courier 16')
d_2_label.grid(column=4, row=3)

btn = ttk.Button(text = "Рассчитать", command=get_param)
btn.grid(row=4, column= 3)

numbers = Text(width=50, height=5, font='Courier 16')
numbers.grid(column= 1, row = 5, columnspan=5, padx=5, pady=5)

root.mainloop()