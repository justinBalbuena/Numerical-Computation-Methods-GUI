import sympy
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

def golden_section_method(a, b, function, tolerance, flag):
    #solution meant to act as a flag in case the solution could not be found
    solution = False
    #separate the min and max method of the golden section to make it easier to read
    match flag:
        case "min":
            solution = golden_ratio_min(a, b, function, tolerance)
        case "max":
            solution = golden_ratio_max(a, b, function, tolerance)
    #what to do dependent of solution
    if solution != False:
        return solution
    else:
        return False
def golden_ratio_min(a,b,function,tolerance):
    # formula for golden section
    golden_section = 1 + sqrt(5)
    golden_section /= 2

    # formula for x1
    x1 = b
    var = b - a
    var /= golden_section
    x1 -= var

    # formula for x2
    x2 = a
    var = (b - a)
    var /= golden_section
    x2 += var

    #y functions with x values
    y1 = function(x1)
    y2 = function(x2)

    i = 1
    while True:
        i += 1
        if y1 >= y2:
            a = x1
            x1 = x2

            #value of x2
            x2 = a
            var = (b - a)
            var /= golden_section
            x2 += var

            y1 = function(x1)
            y2 = function(x2)
        else:
            b = x2
            x2 = x1

            #value of x1
            x1 = b
            var = b - a
            var /= golden_section
            x1 -= var

            y1 = function(x1)
            y2 = function(x2)
        if abs(b-a)<= tolerance:
            x = b+a
            x /= 2
            return x,i
def golden_ratio_max(a,b,function,tolerance):
    golden_section = 1 + sqrt(5)
    golden_section /= 2
    #formula for x1
    x1 = b
    var = b-a
    var /= golden_section
    x1 -= var

    #formula for x2
    x2 = a
    var = (b-a)
    var /= golden_section
    x2 += var
    #find y1 and y2 using the function with the values x1 and x2 plugged in
    y1 = function(x1)
    y2 = function(x2)
    i = 1
    while True:
        i += 1
        if y1 <= y2:
            a = x1
            x1 = x2
            #x2 value
            x2 = a
            var = (b - a)
            var /= golden_section
            x2 += var

            y1 = function(x1)
            y2 = function(x2)
        else:
            b = x2
            x2 = x1

            #formula for x1
            x1 = b
            var = b - a
            var /= golden_section
            x1 -= var

            y1 = function(x1)
            y2 = function(x2)
        if abs(b-a) <= tolerance:
            x = a+b
            x /= 2
            return x,i

def main():
    x = sympy.Symbol('x')
    user_input = input("Enter a function: ")
    function = lambda x: eval(user_input)
    user_a = float(input("Enter a lower bound: "))
    user_b = float(input("Enter a upper bound: "))
    flag = input("will you like to get the maximum or minimum (type max or min): ")
    tolerance_value = 10**-6
    min_or_max,iteration = golden_section_method(user_a,user_b,function,tolerance_value,flag)
    print("the ",flag," of the function is in ", min_or_max," number of iterations are ", iteration)

    user_close = float(input("Enter a number close to a min or max: "))
    n_min_or_max, i = newton_method_min_max(user_close,user_input,tolerance_value)
    print("the root found is: ", n_min_or_max ," and the iterations is: ", i)
def problem2():
    function = 'x**3-4*x'
    function1 = lambda x: eval(function)
    tolerance_value = .000001
    min,i = golden_section_method(-3,3,function1,tolerance_value,"min")
    print("The golden section method ")
    print("the minimum found is: ", min," and the iterations is: ", i)
    max,i = golden_section_method(-3,3,function1,tolerance_value,"max")
    print("The maximum found is ", max," and the iterations is: ", i)
    print("\nThe Newton's method ")
    min,i = newton_method_min_max(3,function,tolerance_value)
    print("the minimum found is: ", min," and the iterations is: ", i)
    max,i = newton_method_min_max(-3,function,tolerance_value)
    print("the maximum found is ", max," and the iterations is: ", i)
