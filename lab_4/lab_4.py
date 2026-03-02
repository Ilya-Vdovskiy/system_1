import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
import math


def calculate(mu, n):
    mx = mu
    dx = 1.0

    numbers = []
    summ = 0
    summ_sq = 0

    for i in range(n):
        x = np.random.randn() + mu
        numbers.append(x)
        summ += x
        summ_sq += x * x

    m = summ / n
    g = summ_sq / n - m ** 2

    delta1 = round(abs(mx - m), 4)
    delta2 = round(abs(dx - g), 4)

    return delta1, delta2, numbers[:20]


def run():
    try:
        l = float(entry_l.get())
        n = int(entry_n.get())

        if n <= 0:
            raise ValueError

        d1, d2, nums = calculate(l, n)

        label_d1.config(text=str(d1))
        label_d2.config(text=str(d2))

        for lbl in outputs:
            lbl.config(text="")

        for i in range(min(len(nums), 20)):
            outputs[i].config(text=f"{nums[i]:.3f}")

    except:
        messagebox.showerror("Ошибка", "Проверь ввод данных")


root = tk.Tk()
root.minsize(650, 500)
root.configure(bg="#f4f6f9")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

style = ttk.Style()
style.theme_use("clam")

main_frame = tk.Frame(root, bg="#f4f6f9")
main_frame.grid(row=0, column=0, sticky="nsew")

main_frame.grid_rowconfigure(3, weight=1)
main_frame.grid_columnconfigure(0, weight=1)


input_frame = tk.Frame(main_frame, bg="#f4f6f9")
input_frame.grid(row=0, column=0, sticky="ew", padx=40, pady=15)

for i in range(4):
    input_frame.grid_columnconfigure(i, weight=1)

label_l = tk.Label(input_frame, text="μ =", bg="#f4f6f9", fg="#2c3e50", font=("Segoe UI", 14, "bold"))
label_l.grid(row=0, column=0, sticky="e", padx=6, ipady=6)

entry_l = ttk.Entry(input_frame, justify="center", font=("Segoe UI", 16, "bold"))
entry_l.grid(row=0, column=1, sticky="ew", padx=10, ipady=8)

label_n = tk.Label(input_frame, text="n =", bg="#f4f6f9", fg="#2c3e50", font=("Segoe UI", 14, "bold"))
label_n.grid(row=0, column=2, sticky="e", padx=6, ipady=6)

entry_n = ttk.Entry(input_frame, justify="center", font=("Segoe UI", 16, "bold"))
entry_n.grid(row=0, column=3, sticky="ew", padx=10, ipady=8)


btn = ttk.Button(main_frame, text="Рассчитать", command=run)
btn.grid(row=1, column=0, sticky="ew", padx=200, pady=10, ipady=6)


output_frame_top = tk.Frame(main_frame, bg="#f4f6f9")
output_frame_top.grid(row=2, column=0, sticky="ew", padx=40, pady=10)

output_frame_top.grid_columnconfigure(0, weight=1)
output_frame_top.grid_columnconfigure(1, weight=1)
output_frame_top.grid_columnconfigure(2, weight=1)
output_frame_top.grid_columnconfigure(3, weight=1)

label_d1_title = tk.Label(output_frame_top,
                          text="Δ1 =",
                          font=("Segoe UI", 14, "bold"),
                          bg="#f4f6f9",
                          fg="#2c3e50")
label_d1_title.grid(row=0, column=0, sticky="e", padx=6, ipady=6)

label_d1 = tk.Label(output_frame_top,
                    font=("Segoe UI", 16, "bold"),
                    bg="white",
                    fg="#2c3e50",
                    relief="groove")

label_d1.grid(row=0, column=1, sticky="ew", padx=10, ipady=12)

label_d2_title = tk.Label(output_frame_top,
                          text="Δ2 =",
                          font=("Segoe UI", 14, "bold"),
                          bg="#f4f6f9",
                          fg="#2c3e50")
label_d2_title.grid(row=0, column=2, sticky="e", padx=6, ipady=6)

label_d2 = tk.Label(output_frame_top,
                    font=("Segoe UI", 16, "bold"),
                    bg="white",
                    fg="#2c3e50",
                    relief="groove")

label_d2.grid(row=0, column=3, sticky="ew", padx=10, ipady=12)


output_frame = tk.Frame(main_frame, bg="#f4f6f9")
output_frame.grid(row=3, column=0, sticky="nsew", padx=40, pady=20)

for i in range(4):
    output_frame.grid_rowconfigure(i, weight=1)

for j in range(5):
    output_frame.grid_columnconfigure(j, weight=1)

outputs = []
for i in range(4):
    for j in range(5):
        label = tk.Label(output_frame,
                         font=("Segoe UI", 16),
                         bg="white",
                         fg="#34495e",
                         relief="ridge")

        label.grid(row=i, column=j, padx=6, pady=6, sticky="nsew")
        outputs.append(label)

root.mainloop()
