from numpy import *
from functions.justin.project6.test import tolerance

def golden_section_method(a, b, function, tolerance, flag):
    solution = False
    match flag:
        case "min":
            solution = golden_ratio_min(a, b, function, tolerance)
        case "max":
            solution = golden_ratio_max(a, b, function, tolerance)
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
    user_input = input("Enter a function: ")
    function = lambda x: eval(user_input)
    user_a = float(input("Enter a lower bound: "))
    user_b = float(input("Enter a upper bound: "))
    flag = input("will you like to get the maximum or minimum (type max or min): ")
    tolerance_value = 10**-6
    min_or_max,iteration = golden_section_method(user_a,user_b,function,tolerance_value,flag)
    print("the ",flag," of the function is in ", min_or_max," number of iterations are ", iteration)
main()





