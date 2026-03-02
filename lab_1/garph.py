import numpy as np
import matplotlib.pyplot as plt

# Создаем данные
x = np.linspace(0, 1, 1000)

# Плотности распределения
f1 = 3 * x**2          # f(x) = 3x²
f2 = 1.5 * np.sqrt(x)  # f(x) = (3/2)√x
f3 = 5 * x**4          # f(x) = 5x⁴

# Функции распределения
F1 = x**3              # F(x) = x³
F2 = x**(3/2)          # F(x) = x^(3/2)
F3 = x**5              # F(x) = x⁵

# Настройка стиля
plt.style.use('seaborn-v0_8-darkgrid')
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# График 1: Плотности распределения
ax1 = axes[0]
ax1.plot(x, f1, 'b-', linewidth=2.5, label=r'$f_1(x) = 3x^2$')
ax1.plot(x, f2, 'orange', linewidth=2.5, label=r'$f_2(x) = \frac{3}{2}\sqrt{x}$')
ax1.plot(x, f3, 'g-', linewidth=2.5, label=r'$f_3(x) = 5x^4$')
ax1.fill_between(x, 0, f1, alpha=0.1, color='blue')
ax1.fill_between(x, 0, f2, alpha=0.1, color='orange')
ax1.fill_between(x, 0, f3, alpha=0.1, color='green')
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('f(x)', fontsize=12)
ax1.set_title('Плотности распределения', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 5.5)

# Добавляем точки в концах
ax1.scatter([1], [3], color='blue', s=80, zorder=5)
ax1.scatter([1], [1.5], color='orange', s=80, zorder=5)
ax1.scatter([1], [5], color='green', s=80, zorder=5)
ax1.text(1.02, 3, '3.0', va='center', fontsize=10)
ax1.text(1.02, 1.5, '1.5', va='center', fontsize=10)
ax1.text(1.02, 5, '5.0', va='center', fontsize=10)

# График 2: Функции распределения
ax2 = axes[1]
ax2.plot(x, F1, 'b-', linewidth=2.5, label=r'$F_1(x) = x^3$')
ax2.plot(x, F2, 'orange', linewidth=2.5, label=r'$F_2(x) = x^{3/2}$')
ax2.plot(x, F3, 'g-', linewidth=2.5, label=r'$F_3(x) = x^5$')
ax2.plot([0, 1], [0, 1], 'r--', alpha=0.5, label='Диагональ')
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('F(x)', fontsize=12)
ax2.set_title('Функции распределения', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11, loc='lower right')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)

# Добавляем текст с наклонами
ax2.text(0.15, 0.15**3, 'f(0.15)=0.0675', fontsize=9, color='blue', rotation=10)
ax2.text(0.15, 0.15**(3/2), 'f(0.15)=0.581', fontsize=9, color='orange', rotation=25)
ax2.text(0.15, 0.15**5, 'f(0.15)=0.000076', fontsize=9, color='green', rotation=2)

plt.tight_layout()
plt.show()

# Дополнительный график: сравнение всех функций
fig2, ax3 = plt.subplots(figsize=(10, 8))

# Рисуем все 6 функций на одном графике
ax3.plot(x, f1, 'b-', linewidth=2, label=r'$f_1(x)=3x^2$')
ax3.plot(x, f2, 'orange', linewidth=2, label=r'$f_2(x)=\frac{3}{2}\sqrt{x}$')
ax3.plot(x, f3, 'g-', linewidth=2, label=r'$f_3(x)=5x^4$')
ax3.plot(x, F1, 'b--', linewidth=2, label=r'$F_1(x)=x^3$')
ax3.plot(x, F2, 'orange', '--', linewidth=2, label=r'$F_2(x)=x^{3/2}$')
ax3.plot(x, F3, 'g--', linewidth=2, label=r'$F_3(x)=x^5$')

ax3.set_xlabel('x', fontsize=12)
ax3.set_ylabel('y', fontsize=12)
ax3.set_title('Все функции распределения и их плотности', fontsize=14, fontweight='bold')
ax3.legend(fontsize=10, loc='upper left')
ax3.grid(True, alpha=0.3)
ax3.set_xlim(0, 1)

# Добавляем вертикальные линии для сравнения
for x_val in [0.2, 0.5, 0.8]:
    ax3.axvline(x=x_val, color='gray', linestyle=':', alpha=0.5)
    ax3.text(x_val, 5.2, f'x={x_val}', ha='center', fontsize=9)

plt.tight_layout()
plt.show()

# Табличные значения для x=0.2, 0.5, 0.8
print("Таблица значений при различных x:")
print("=" * 50)
print("x = 0.2:")
print(f"  f₁(0.2) = {3*0.2**2:.4f}   F₁(0.2) = {0.2**3:.4f}")
print(f"  f₂(0.2) = {1.5*np.sqrt(0.2):.4f}   F₂(0.2) = {0.2**(3/2):.4f}")
print(f"  f₃(0.2) = {5*0.2**4:.4f}   F₃(0.2) = {0.2**5:.4f}")
print()
print("x = 0.5:")
print(f"  f₁(0.5) = {3*0.5**2:.4f}   F₁(0.5) = {0.5**3:.4f}")
print(f"  f₂(0.5) = {1.5*np.sqrt(0.5):.4f}   F₂(0.5) = {0.5**(3/2):.4f}")
print(f"  f₃(0.5) = {5*0.5**4:.4f}   F₃(0.5) = {0.5**5:.4f}")
print()
print("x = 0.8:")
print(f"  f₁(0.8) = {3*0.8**2:.4f}   F₁(0.8) = {0.8**3:.4f}")
print(f"  f₂(0.8) = {1.5*np.sqrt(0.8):.4f}   F₂(0.8) = {0.8**(3/2):.4f}")
print(f"  f₃(0.8) = {5*0.8**4:.4f}   F₃(0.8) = {0.8**5:.4f}")