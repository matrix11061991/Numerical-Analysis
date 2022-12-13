# Differentiation
Numerical differentiation is a technique used in mathematics to approximate the derivative of a function at a given point. 
In `Python`, there are several ways to approximate the derivative of a function numerically.
One of the simplest methods is to use the following formula to calculate the derivative of a function f at a point `x`:

`derivée ≈ (f(x + h) - f(x)) / h`

```python
def derivee(f, x, h=1e-6):
  return (f(x + h) - f(x)) / h
```
To use this function, you can define a function f and pass its value of x to the derivative function:
```python
# définir la fonction f
def f(x):
  return pow(x,3)
# calculate the derivative at x = 2
derivee(f, 2)
```

