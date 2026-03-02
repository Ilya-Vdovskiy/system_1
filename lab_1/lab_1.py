import pandas as pd
from solutions import solutions

N_values = [100, 500, 1000, 10000]
rows = []

for N in N_values:
    mx, m, d1, dx, g, d2 = solutions.variant_11(N)
    rows.append([N, m, mx, d1, g, dx, d2])

df = pd.DataFrame(rows, columns=["N", "m", "Mx", "delta1", "g", "Dx", "delta2"])
df_round = df.round(4)

print("=" * 80)
print("Результаты моделирования")
print("=" * 80)

print(f"{'N':<10} {'m':<12} {'Mx':<12} {'delta1':<12} {'g':<12} {'Dx':<12} {'delta2':<12}")
print("-" * 80)

for _, row in df_round.iterrows():
    print(f"{int(row['N']):<10} {row['m']:<12.4f} {row['Mx']:<12.4f} {row['delta1']:<12.4f} {row['g']:<12.4f} {row['Dx']:<12.4f} {row['delta2']:<12.4f}")

print("=" * 80)
