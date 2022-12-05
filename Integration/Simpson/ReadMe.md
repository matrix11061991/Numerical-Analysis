# Simpson's method

Simpson's method allows the approximate calculation of an integral with the following formula:

<img src="https://latex.codecogs.com/svg.image?\int_{a}^{b}&space;f(x)&space;dx&space;\approx&space;\frac{b-a}{6}\left[f(a)&space;&plus;&space;4f\left(\frac{a&plus;b}{2}\right)&plus;f(b)\right]"/>

To obtain Simpson's formula, we will carry out an interpolation with a polynomial of degree 2. A polynomial being a function very easy to integrate, we approach the integral of the function over the interval [a,b], by the integral of the polynomial over this same interval.
## Interpolation by a polynomial of degree 2
An interpolation which passes through 3 points can be carried out thanks to a polynomial of degree 2. In the case of Simpson's method, the polynomial will take the same values as f at the abscissa points a, b and 
<img src="https://latex.codecogs.com/svg.image?m&space;=&space;(a&space;&plus;&space;b)/2"/>
The technique used to determine the polynomial is based on the Lagrange polynomials, we speak of Lagrangian interpolation.

Lagrange polynomials of degree 2 have the characteristic of taking the value 1 for only one of the 3 abscissas and the value 0 for the other 2. We thus define 3 polynomials:

<img src="https://latex.codecogs.com/svg.image?l_0(x)&space;=&space;\frac{(x-m)(x-b)}{(a-m)(a-b)}"/>    which takes the value 1 in <img src="https://latex.codecogs.com/svg.image?x=a"/> and 0 in m and b

<img src="https://latex.codecogs.com/svg.image?l_1(x)&space;=&space;\frac{(x-a)(x-b)}{(m-a)(m-b)}"/>    which takes the value 1 in <img src="https://latex.codecogs.com/svg.image?x=m"/> and 0 in a and b

<img src="https://latex.codecogs.com/svg.image?l_2(x)&space;=&space;\frac{(x-a)(x-m)}{(b-a)(b-m)}"/>    which takes the value 1 in <img src="https://latex.codecogs.com/svg.image?x=b"/> and 0 in a and m

### Visualization of Lagrange polynomials

```python
from pylab import *
```
The polynomial P of degree 2 which takes the same values as f at the abscissa points a, b and m can be written in the following form:

<img src="https://latex.codecogs.com/svg.image?P(x)=f(a)\frac{(x-m)(x-b)}{(a-m)(a-b)}&plus;f(m)\frac{(x-a)(x-b)}{(m-a)(m-b)}&plus;f(b)\frac{(x-a)(x-m)}{(b-a)(b-m)}"/>

The calculation of this integral is not immediate and we will detail a way to carry out this calculation.



### Example of Lagrange interpolation with a polynomial of degree 2
```python
from pylab import *
```

## Integration of Lagrange polynomials
A polynomial being a function very easy to integrate, we approach the integral of the function over the interval [a,b], by the integral of P over this same interval. For this, we will calculate the integrals of the 3 Lagrange polynomials.
Let us first consider the calculation of the integral of the Lagrange polynomial <img src="https://latex.codecogs.com/svg.image?l_2"/>.

<img src="https://latex.codecogs.com/svg.image?\int_{a}^{b}&space;l_2(x)&space;dx&space;=&space;\int_{a}^{b}&space;\frac{(x-a)(x-m)}{(b-a)(b-m)}&space;dx."/>
