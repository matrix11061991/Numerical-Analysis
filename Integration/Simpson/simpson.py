class Simpson:
  def __init__(self, f, a, b):
    self.f = f
    self.a = a
    self.b = b

  def integrate(self):
    h = (self.b - self.a) / 2
    return h / 3 * (self.f(self.a) + 4 * self.f((self.a + self.b) / 2) + self.f(self.b))

def f(x):
  return x**2

s = Simpson(f, 0, 1)
result = s.integrate()

print(result)
