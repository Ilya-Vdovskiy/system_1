import random
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox


def xi():
    return sum(random.random() for _ in range(12)) - 6

def zi(a, sigma):
    return a + xi() * sigma


def calculate(n, a, sigma):
    data = [zi(a, sigma) for _ in range(n)]

    m = sum(data) / n
    g = sum(x**2 for x in data) / n - m**2

    MX = a
    DX = sigma ** 2

    d1 = abs(MX - m)
    d2 = abs(DX - g)

    return data[:20], m, g, d1, d2


def run():
    try:
        n = int(entry_n.get())
        a = float(entry_a.get())
        sigma = float(entry_sigma.get())

        if n <= 0 or sigma <= 0:
            raise ValueError

        nums, m, g, d1, d2 = calculate(n, a, sigma)

        label_m.config(text=f"m = {m:.4f}")
        label_g.config(text=f"g = {g:.4f}")
        label_d1.config(text=f"d1 = {d1:.4f}")
        label_d2.config(text=f"d2 = {d2:.4f}")

        for lbl in outputs:
            lbl.config(text="")

        for i in range(len(nums)):
            outputs[i].config(text=f"{nums[i]:.3f}")

    except:
        messagebox.showerror("Ошибка", "Проверь ввод данных")


root = tk.Tk()
root.title("Моделирование нормального распределения")
root.minsize(700, 500)
root.configure(bg="#f4f6f9")


root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

style = ttk.Style()
style.theme_use("clam")


input_frame = tk.Frame(root, bg="#f4f6f9")
input_frame.grid(row=0, column=0, sticky="ew", padx=40, pady=15)

for i in range(6):
    input_frame.grid_columnconfigure(i, weight=1)

label_n = tk.Label(input_frame, text="n =", bg="#f4f6f9", fg="#2c3e50", font=("Segoe UI", 14, "bold"))
label_n.grid(row=0, column=0, sticky="e", padx=6, ipady=6)

entry_n = ttk.Entry(input_frame, justify="center", font=("Segoe UI", 14))
entry_n.grid(row=0, column=1, sticky="ew", padx=10, ipady=6)
entry_n.insert(0, "10000")

label_a = tk.Label(input_frame, text="a =", bg="#f4f6f9", fg="#2c3e50", font=("Segoe UI", 14, "bold"))
label_a.grid(row=0, column=2, sticky="e", padx=6, ipady=6)

entry_a = ttk.Entry(input_frame, justify="center", font=("Segoe UI", 14))
entry_a.grid(row=0, column=3, sticky="ew", padx=10, ipady=6)
entry_a.insert(0, "0")

label_sigma = tk.Label(input_frame, text="sigma =", bg="#f4f6f9", fg="#2c3e50", font=("Segoe UI", 14, "bold"))
label_sigma.grid(row=0, column=4, sticky="e", padx=6, ipady=6)

entry_sigma = ttk.Entry(input_frame, justify="center", font=("Segoe UI", 14))
entry_sigma.grid(row=0, column=5, sticky="ew", padx=10, ipady=6)
entry_sigma.insert(0, "1")


btn = ttk.Button(root, text="Рассчитать", command=run)
btn.grid(row=1, column=0, sticky="ew", padx=200, pady=10, ipady=6)


stat_frame = tk.Frame(root, bg="#f4f6f9")
stat_frame.grid(row=2, column=0, sticky="ew", padx=40, pady=10)

for i in range(2):
    stat_frame.grid_columnconfigure(i, weight=1)

label_m = tk.Label(stat_frame, font=("Segoe UI", 14, "bold"),
                   bg="white", relief="groove")
label_m.grid(row=0, column=0, sticky="ew", padx=10, ipady=10)

label_g = tk.Label(stat_frame, font=("Segoe UI", 14, "bold"),
                   bg="white", relief="groove")
label_g.grid(row=0, column=1, sticky="ew", padx=10, ipady=10)

label_d1 = tk.Label(stat_frame, font=("Segoe UI", 14, "bold"),
                    bg="white", relief="groove")
label_d1.grid(row=1, column=0, sticky="ew", padx=10, pady=5, ipady=10)

label_d2 = tk.Label(stat_frame, font=("Segoe UI", 14, "bold"),
                    bg="white", relief="groove")
label_d2.grid(row=1, column=1, sticky="ew", padx=10, pady=5, ipady=10)


output_frame = tk.Frame(root, bg="#f4f6f9")
output_frame.grid(row=3, column=0, sticky="nsew", padx=40, pady=20)

for i in range(4):
    output_frame.grid_rowconfigure(i, weight=1)

for j in range(5):
    output_frame.grid_columnconfigure(j, weight=1)

outputs = []

for i in range(4):
    for j in range(5):
        label = tk.Label(output_frame,
                         font=("Segoe UI", 12),
                         bg="white",
                         fg="#34495e",
                         relief="ridge")

        label.grid(row=i, column=j, padx=6, pady=6, sticky="nsew")
        outputs.append(label)

root.mainloop()
