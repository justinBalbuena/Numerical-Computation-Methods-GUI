from scipy.optimize import fsolve
from sympy import *
from math import *
#without math, it will not recognize sin,cos,tan
#this function give you the true root of the function near a point probably more accurate then the function
#created in class

def find_roots(user_function,x0):
    x = symbols('x')
    user_function = user_function.replace('e', 'E')
    user_expression = sympify(user_function)

    # Create a callable function for the user's expression
    user_func = lambdify(x, user_expression)

    root = fsolve(user_func,x0)
    return root[0]