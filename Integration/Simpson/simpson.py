class Simpson:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def f(x):
        # Définissez ici la fonction que vous souhaitez intégrer
        return x**2

    def integrate(self):
        h = (self.b - self.a) / self.n

        # Appliquez la formule de la méthode de Simpson pour calculer l'intégrale
        integral = (self.f(self.a) + self.f(self.b))
        for i in range(1, self.n, 2):
            integral += 4 * self.f(self.a + i * h)
        for i in range(2, self.n-1, 2):
            integral += 2 * self.f(self.a + i * h)

        integral = integral * h / 3

        return integral

# Utilisez la classe Simpson pour calculer l'intégrale d'une fonction
simp = Simpson(0, 1, 100)
print(simp.integrate())
