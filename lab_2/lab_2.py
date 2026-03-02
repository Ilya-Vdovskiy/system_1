import random
import pandas as pd

def variant_5(N):
    x = [1, -1, 2]
    k1 = k2 = k3 = 0
    p = [0.2, 0.4, 0.4]
    for i in range(N):
        r = random.random()
        if r >= 0 and r < p[0]:
            k1 += 1
        elif r >= p[0] and r < p[0] + p[1]:
            k2 += 1
        elif r >= p[0] + p[1] and r < 1:
            k3 += 1
    
    # Теоретические характеристики
    mx = x[0] * p[0] + x[1] * p[1] + x[2] * p[2]
    dx = x[0] ** 2 * p[0] + x[1] ** 2 * p[1] + x[2] ** 2 * p[2] - mx ** 2
    
    # Выборочные характеристики
    m = (k1 * x[0] + k2 * x[1] + k3 * x[2]) / N
    g = (k1 * x[0] ** 2 + k2 * x[1] ** 2 + k3 * x[2] ** 2) / N - m ** 2
    
    return round(mx,4), round(m,4), round(abs(mx-m),4), round(dx,4), round(g, 4), round(abs(dx-g),4), k1, k2, k3


N_values = [100, 500, 1000, 10000, 1000000]
rows = []

print("=" * 100)
print("РЕЗУЛЬТАТЫ МОДЕЛИРОВАНИЯ ДЛЯ ДИСКРЕТНОЙ СЛУЧАЙНОЙ ВЕЛИЧИНЫ")
print("=" * 100)

# Сбор и вывод данных в виде таблицы
print(f"{'N':<12} {'m':<12} {'Mx':<12} {'Δ1':<12} {'g':<12} {'Dx':<12} {'Δ2':<12} {'k1(0.3)':<10} {'k2(0.6)':<10} {'k3(0.1)':<10}")
print("-" * 100)

for N in N_values:
    mx, m, d1, dx, g, d2, k1, k2, k3 = variant_5(N)
    print(f"{N:<12} {m:<12.4f} {mx:<12.4f} {d1:<12.4f} {g:<12.4f} {dx:<12.4f} {d2:<12.4f} {k1:<10} {k2:<10} {k3:<10}")

print("=" * 100)

# Дополнительная таблица с частотами и вероятностями
print("\n" + "=" * 80)
print("АНАЛИЗ ЧАСТОТ")
print("=" * 80)

print(f"{'N':<12} {'Категория':<12} {'Наблюдаемая частота':<20} {'Ожидаемая частота':<20} {'Отклонение':<15}")
print("-" * 80)

for N in N_values:
    mx, m, d1, dx, g, d2, k1, k2, k3 = variant_5(N)
    
    # Для каждой категории
    categories = [
        ("k1 (x=31)", k1, 0.1 * N),
        ("k2 (x=-17)", k2, 0.8 * N),
        ("k3 (x=12)", k3, 0.1 * N)
    ]
    
    for cat_name, observed, expected in categories:
        deviation = observed - expected
        print(f"{N:<12} {cat_name:<12} {observed:<20} {expected:<20.1f} {deviation:<+15.1f}")
    print("-" * 40)

