from numpy import *
import sympy as sp
from sympy import lambdify

def newton_method_min_max(x0,function,tolerance):
    #creates derivatives 1st and 2nd
    f_dx = sp.diff(function,'x')
    f_2dx = sp.diff(f_dx,'x')
    #allows for derivatives to be used as a function
    f_dx = lambdify('x',f_dx,)
    f_2dx = lambdify('x',f_2dx)
    #sets value for a
    a = .999
    #sets the 1st value for xk and xk+1
    x_k = x0
    x_k1 = x_k
    x_k1 -= a * f_dx(x_k)/f_2dx(x_k)
    #inital value for iterations
    i = 1
    while a > 0:
        #if both xk and xk+1 subtracted is less than tolerance then x_k1 is the solution
        if abs(x_k1 - x_k) < tolerance:
            return x_k1,i
        #else set xk = xk+1 and does the same as if out of the while loop
        else:
            a -= .001
            i += 1
            x_k = x_k1
            x_k1 = x_k
            x_k1 -= a * f_dx(x_k) / f_2dx(x_k)
