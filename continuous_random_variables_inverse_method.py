import numpy as np

ln2 = np.log(2)
a, b = 1, 2

Mx_exact = (b - a) / ln2
Dx_exact = ((b**2 - a**2) / (2 * ln2)) - Mx_exact**2

np.random.seed(42)

print("="*120)
print("Лабораторная работа №2. Моделирование случайной величины методом обратной функции")
print("Плотность распределения: f(x) = 1/(x·ln(2)), x ∈ [1, 2]")
print("="*120)
print(f"{'N':^6} | {'Математическое ожидание':^38} | {'Дисперсия':^38} | {'Первые 15 значений x':^25}")
print(f"{'':^6} | {'Точное':^10} {'Оценка':^10} {'ε':^8} {'δ%':^8} | {'Точное':^10} {'Оценка':^10} {'ε':^8} {'δ%':^8} | {'(первые 15 из N)':^25}")
print("-"*120)

for N in [500, 1000]:
    u = np.random.uniform(0, 1, N)
    x = a * np.exp(u * ln2)
    
    Mx_est = np.mean(x)
    Dx_est = np.var(x, ddof=1)
    
    eps_Mx = Mx_est - Mx_exact
    eps_Dx = Dx_est - Dx_exact
    rel_Mx = abs(eps_Mx / Mx_exact) * 100
    rel_Dx = abs(eps_Dx / Dx_exact) * 100
    
    first_15_str = " ".join([f"{val:.4f}" for val in x[:15]])
    
    print(f"{N:^6} | {Mx_exact:^10.6f} {Mx_est:^10.6f} {eps_Mx:^+8.6f} {rel_Mx:^8.2f} | "
          f"{Dx_exact:^10.6f} {Dx_est:^10.6f} {eps_Dx:^+8.6f} {rel_Dx:^8.2f} | {first_15_str:^25}")

print("="*120)
print()

print("ФОРМУЛЫ И ВЫЧИСЛЕНИЯ:")
print(f"1. ln(2) = {ln2:.6f}")
print(f"2. Точное математическое ожидание: Mx = (b-a)/ln(2) = ({b}-{a})/{ln2:.6f} = {Mx_exact:.6f}")
print(f"3. Точная дисперсия: Dx = (b²-a²)/(2·ln(2)) - Mx² = ({b}²-{a}²)/(2·{ln2:.6f}) - ({Mx_exact:.6f})² = {Dx_exact:.6f}")
print()

print("ВЫВОДЫ:")
print("1. Метод обратной функции: x = a * exp(u * ln(2)), где u ~ Uniform(0,1)")
print("2. Оценки сходятся к теоретическим значениям при увеличении N")
print("3. Относительные ошибки уменьшаются с ростом объема выборки")
print("4. Все сгенерированные значения x ∈ [1, 2], что соответствует заданному интервалу")