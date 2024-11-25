import re
#watch https://www.youtube.com/watch?v=K8L6KVGG-7o to have a better understanding in case you need to modify something
def transform_math_expression(expression):
    #finds a case where e in the string and converts to E since sympy does not recognize
    #e as the constant,but it does for E
    expression = re.sub(r'([e])',r'E',expression)

    return expression