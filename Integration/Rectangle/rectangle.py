from math import *
def LeftRectangle( f, a, b, n ):
    h = (b - a)/n
    s = sum(map(f,(a + h*i for i in range(n))))
    return s * h
print(LeftRectangle(sin, 0., tau, 100))