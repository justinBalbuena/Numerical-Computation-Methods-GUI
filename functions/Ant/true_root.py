from scipy.optimize import fsolve
from math import *
def find_roots(user_function,x0):
    function = lambda x: eval(user_function)
    root = fsolve(function,x0)
    return root[0]