import scipy.integrate as integrate

def f(x):
    # La fonction à intégrer
    return x**2

a = 0 # limite inférieure de l'intégrale
b = 2 # limite supérieure de l'intégrale

approximation = integrate.trapezoid(f, a, b)

print(approximation)
