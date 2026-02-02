import random

def get_m(N):
    return sum(N) / len(N)

def get_p(N, m):
    return sum(x ** 2 for x in N) / len(N) - m ** 2

def get_res(size):
    N = []

    for i in range(size):
        rand = random.random()
        N.append(rand**(1/3))
    
    Mx = 3/4
    Dx = 3/80

    m = get_m(N)
    p = get_p(N, m)

    print("%d \t| %.6f \t| %.6f \t| %.6f \t| %.6f \t| %.6f \t| %.6f \t|" % (len(N), Mx, m, abs(Mx-m), Dx, p, abs(Dx-p)))

print("N \t| MX\t\t| m\t\t| delta 1\t| DX\t\t| g\t\t| delta 2 \t|")
get_res(100)
get_res(1000)
get_res(10000)
get_res(100000)