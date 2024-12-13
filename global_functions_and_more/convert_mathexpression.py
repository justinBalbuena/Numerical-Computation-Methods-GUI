import re
#watch https://www.youtube.com/watch?v=K8L6KVGG-7o to have a better understanding in case you need to modify something
def transform_math_expression(expression):
    #finds the pattern \d+ any digit and x like 2x and then replaces it with 2*x
    expression = re.sub(r'(\d+)([x])',r'\1*x',expression)
    #finds the pattern any digit and then replaces it with the digit * sin
    expression = re.sub(r'(\d+)(sin)',r'\1*sin',expression)
    expression = re.sub(r'(\d+)(cos)',r'\1*cos',expression)

    #finds pattern with any digit and ^ and add ** so 100123^x = 100123**x
    expression = re.sub(r'(\d+)([\^])',r'\1**',expression)
    #finds pattern with any x and ^ transforms it. So x^123131413 = x**123131413
    expression = re.sub(r'([x])([\^])',r'\1**',expression)
    expression = re.sub(r'([)])([\^])',r'\1**',expression)
    #find pattern with r and ^ and transforms it. so e^12321132 = e**12321132
    expression = re.sub(r'([e])([\^])', r'\1**', expression)
    expression = re.sub(r'([e])',r'E',expression)
    return expression
# Purpose of this is to make it easier for the user to input mathematical expression like 2x instead of 2*x
# In the case where you have used sympy where e constant is E instead of e this could be used to make it consistent throughout