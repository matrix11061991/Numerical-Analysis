import math

def simpson(f, a, b):
  return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

# Appliquons cette méthode pour calculer l'intégrale de f(x) = x^2 sur l'intervalle [0, 2]

def f(x):
  return x * x

a = 0
b = 2

résultat = simpson(f, a, b)

print("L'intégrale de f(x) = x^2 sur l'intervalle [0, 2] est approximativement égale à", résultat)
