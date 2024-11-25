from scipy.optimize import fsolve
from math import *
#without math, it will not recognize sin,cos
#this function give you the true root of the function near a point probably more accurate then the function
#created in class

def find_roots(user_function,x0):
    function = lambda x: eval(user_function)
    root = fsolve(function,x0)
    return root[0]