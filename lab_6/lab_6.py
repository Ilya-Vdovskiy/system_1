import random
import tkinter as tk
from tkinter import messagebox


def xi():
    return sum(random.random() for _ in range(12)) - 6


def zi(a, sigma):
    return a + xi() * sigma


def calculate(n, a, sigma):
    return [zi(a, sigma) for _ in range(n)]


def calculate_ascent_measure(heights):
    diffs = [heights[i + 1] - heights[i] for i in range(len(heights) - 1)]
    total_change = sum(abs(diff) for diff in diffs)

    if total_change == 0:
        return 0.0

    positive_change = sum(max(diff, 0) for diff in diffs)
    return positive_change / total_change


def build_histogram():
    try:
        n = int(entry_n.get())
        a = float(entry_a.get())
        sigma = float(entry_sigma.get())

        if n <= 0:
            raise ValueError("n должно быть > 0")

        m = 6
        data = calculate(n, a, sigma)

        xmin = min(data)
        xmax = max(data)

        if xmin == xmax:
            xmax = xmin + 1

        h = (xmax - xmin) / m
        heights = [0] * m

        for value in data:
            index = int((value - xmin) / h)
            if index >= m:
                index = m - 1
            heights[index] += 1

        ascent_measure = calculate_ascent_measure(heights)
        label_ascent.config(text=f"Мера восхождения: {ascent_measure:.4f}")

        draw_histogram(heights, xmin, xmax)

    except ValueError as error:
        messagebox.showerror("Ошибка", str(error))


def draw_histogram(heights, xmin, xmax):
    canvas.delete("all")

    width = 600
    height = 400
    margin = 50
    plot_height = height - 2 * margin
    plot_width = width - 2 * margin
    max_height = max(heights)
    bar_width = plot_width / len(heights)
    bin_width = (xmax - xmin) / len(heights)

    canvas.create_line(margin, margin, margin, height - margin, width=2)
    canvas.create_line(margin, height - margin, width - margin, height - margin, width=2)

    for i in range(6):
        y = height - margin - i * plot_height / 5
        value = max_height * i / 5 if max_height else 0
        canvas.create_line(margin - 5, y, margin, y, width=1)
        canvas.create_text(margin - 25, y, text=f"{value:.0f}", font=("Arial", 8))

    for i, h_val in enumerate(heights):
        bar_height = (h_val / max_height) * plot_height if max_height else 0

        x1 = margin + i * bar_width
        y1 = height - margin - bar_height
        x2 = x1 + bar_width - 5
        y2 = height - margin

        canvas.create_rectangle(x1, y1, x2, y2, fill="skyblue", outline="black")
        canvas.create_text((x1 + x2) / 2, y1 - 10, text=str(h_val), font=("Arial", 9))

        left_border = xmin + i * bin_width
        canvas.create_text((x1 + x2) / 2, height - margin + 15, text=f"{left_border:.2f}", font=("Arial", 8))

    canvas.create_text(width - margin, height - margin + 15, text=f"{xmax:.2f}", font=("Arial", 8))
    canvas.create_text(width / 2, height - 15, text="Интервалы X", font=("Arial", 10, "bold"))
    canvas.create_text(18, height / 2, text="Частота", angle=90, font=("Arial", 10, "bold"))


root = tk.Tk()
root.title("Гистограмма нормального распределения")
root.geometry("700x600")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="n:").grid(row=0, column=0)
entry_n = tk.Entry(frame)
entry_n.insert(0, "1000")
entry_n.grid(row=0, column=1)

tk.Label(frame, text="a:").grid(row=0, column=2)
entry_a = tk.Entry(frame)
entry_a.insert(0, "0")
entry_a.grid(row=0, column=3)

tk.Label(frame, text="sigma:").grid(row=0, column=4)
entry_sigma = tk.Entry(frame)
entry_sigma.insert(0, "1")
entry_sigma.grid(row=0, column=5)

tk.Button(root, text="Построить", command=build_histogram).pack(pady=10)

label_ascent = tk.Label(root, text="Мера восхождения: -", font=("Arial", 11))
label_ascent.pack(pady=5)

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

root.mainloop()
