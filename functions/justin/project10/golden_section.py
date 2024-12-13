from sympy import *


def golden_section(a, b, user_function, type, tolerance):
    golden_num = 1.618

    user_expression = lambda x: eval(user_function)

    x1 = b - (b - a) / golden_num
    x2 = a + (b - a) / golden_num
    y1 = user_expression(x1)
    y2 = user_expression(x2)
    iterations = 0

    match type:
        case 'min':
            while abs(b - a) > tolerance:
                iterations += 1

                if y1 >= y2:
                    a = x1
                    x1 = x2
                    x2 = a + ((b - a) / golden_num)
                    y1 = user_expression(x1)
                    y2 = user_expression(x2)
                else:
                    b = x2
                    x2 = x1
                    x1 = b - (b - a) / golden_num
                    y1 = user_expression(x1)
                    y2 = user_expression(x2)
        case 'max':
            while abs(b - a) > tolerance:
                iterations += 1

                if y1 <= y2:
                    a = x1
                    x1 = x2
                    x2 = a + ((b - a) / golden_num)
                    y1 = user_expression(x1)
                    y2 = user_expression(x2)
                else:
                    b = x2
                    x2 = x1
                    x1 = b - (b - a) / golden_num
                    y1 = user_expression(x1)
                    y2 = user_expression(x2)

    return (a + b) / 2, user_expression((a + b) / 2), iterations

