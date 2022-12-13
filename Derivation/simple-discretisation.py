def derivee(f, x, h = 1e-6):
  return (f(x + h) - f(x)) / h
# To use this function, you can define a function f and pass its value of x to the derivative function:
# define the function f
def f(x):
  return pow(x,3)
# calculate the derivative function for x = 2
derivee(f, 2)

