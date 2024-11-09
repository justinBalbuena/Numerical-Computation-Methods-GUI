from math import *
from sympy import symbols
from sympy.stats import Trapezoidal

x = symbols("x")
def trapezoidal_rule(x0,x1,function):
    h = (x1 - x0) / 20
    sum_of_trapezoidal = 0
    for i in range(1,20):
        x_k = (i * h) + x0
        sum_of_trapezoidal += function(x_k)
    solution = h/2
    solution *= function(x0) + 2*sum_of_trapezoidal
    return solution
def simpson_rule(x0,x2,function):
    n = 20
    h = (x2 - x0) / n
    x_n =  x0+(n*h)
    sum_of_simpson1 = 0
    sum_of_simpson2 = 0
    e1 = int(n/2 -1)
    e2 = int(n/2)

    for i in range(1,e1+1):
        x_k = x0
        x_k += 2*i*h
        sum_of_simpson1 += function(x_k)

    for i in range(1,e2+1):
        x_k = x0
        x_k += 2*i-1
        x_k *= h
        sum_of_simpson2 += function(x_k)

    solution = h/3
    solution *= function(x0) + 2*sum_of_simpson1 + 4*sum_of_simpson2 + function(x_n)
    return solution
print("Integrates continuous function using both trapezoidal and simpson rule")
user_function = input("Enter a function (format 2*x not 2x): ")
function = lambda x: eval(user_function)
solution = trapezoidal_rule(0,pi,function)
solution1 = simpson_rule(0,pi,function)
print("Trapezoidal integration: ", solution, "Simpson rule: ", solution1)


