from numpy import *

def golden_section_method(a, b, user_function, tolerance, flag):
    #solution meant to act as a flag in case the solution could not be found
    solution = False
    function = lambda x: eval(user_function)
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
