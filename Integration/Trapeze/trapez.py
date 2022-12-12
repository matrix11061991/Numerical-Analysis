import math

def trapèze(f, a, b, n):
  h = (b - a) / n
  s = 0.5 * (f(a) + f(b))
  for i in range(1, n):
    s += f(a + i * h)
  return s * h

# Appliquons cette méthode pour calculer l'intégrale de f(x) = x^2 sur l'intervalle [0, 2]

def f(x):
  return x * x

a = 0
b = 2
n = 100

résultat = trapèze(f, a, b, n)

print("L'intégrale de f(x) = x^2 sur l'intervalle [0, 2] est approximativement égale à", résultat)

