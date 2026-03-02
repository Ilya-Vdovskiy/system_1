import numpy as np
import pandas as pd


def variant_11(N):
    mx = (5+1) / (5 + 2)
    dx = (5 + 1) / ((5 + 3) * (5 + 2) ** 2)

    r = np.random.rand(N)
    x = r**(1/(5+1))
    m = round(1/N * np.sum(x), 4)
    g = round(1/N * np.sum(x*x)-m*m, 4)

    delta1 = round(abs((5+1)/(5+2) - m), 4)
    delta2 = round(abs((5+1)/((5+3)*(5+2)**2) - g),4)

    return round(mx, 4), round(m,4), round(delta1,4), round(dx, 4), round(g,4), round(delta2,4)

def variant_19(N):
    #mx = (n+1) / (n + 2)
    #dx = (n + 1) / ((n + 3) * (n + 2) ** 2)
    mx = 3/5
    dx = 12/175
    r = np.random.rand(N)
    x = 3 * np.sqrt(r) / 2 
    m = np.mean(x)
    g = np.var(x)
    delta1 = abs(mx - m)
    delta2 = abs(dx - g)
    return round(mx, 4), round(m,4), round(delta1,4), round(dx, 4), round(g,4), round(delta2,4)



def variant_38(N):
    #mx = (n+1) / (n + 2)
    #dx = (n + 1) / ((n + 3) * (n + 2) ** 2)
    mx = 5/6
    dx = 5/252
    r = np.random.rand(N)
    x = 5*(r**4)
    m = round(1/N * np.sum(x), 4)
    g = round(1/N * np.sum(x*x)-m*m, 4)

    delta1 = round(mx - m, 4)
    delta2 = round(dx - g,4)
    return round(mx, 4), round(m,4), round(delta1,4), round(dx, 4), round(g,4), round(delta2,4)