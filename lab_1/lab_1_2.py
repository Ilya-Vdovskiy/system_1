import random

def get_m(N):
    return sum(N) / len(N)

def get_g(N, m):
    return sum(x ** 2 for x in N) / len(N) - m ** 2

def get_res(size):
    N = []

    for i in range(size):
        rand = random.random()
        N.append(rand ** 2/3)

    MX = 3/5
    DX = 12/175

    m = get_m(N)
    g = get_g(N, m)

    print("%d \t| %.6f \t| %.6f \t| %.6f \t| %.6f \t| %.6f \t| %.6f \t|" % (len(N), MX, m, abs(MX-m), DX, g, abs(DX-g)))

print("N \t| MX\t\t| m\t\t| delta 1\t| DX\t\t| g\t\t| delta 2 \t|")
get_res(100)
get_res(1000)
get_res(10000)
get_res(100000)

def print_first_values(size, q):
    print(f"\nПервые {q} значений из N={size}:")
    N = []
    for i in range(size):
        rand = random.random()
        N.append(rand**(2/3))
    
    for i in range(min(q, len(N))):
        print(f"  X{i+1} = {N[i]:.6f}")

print_first_values(100, 12)