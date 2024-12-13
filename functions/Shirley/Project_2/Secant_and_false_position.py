import math
from sympy import * #using this library for the function

def secant_method(x0, x1, tolerance, flag, math_function):  #my secant function declaring the variables I'll use
    # sets up a function using lambdify to set up the user's given function for usability
    x = symbols('x')
    math_function = math_function.replace('e', 'E')
    user_expression = sympify(math_function)
    # Create a callable function for the user's expression
    original_function = lambdify(x, user_expression)

    count = 0  #setting my counter to 0
    while True: #will run until it fits the one of the requirements
        if abs(original_function(x0)) < abs(original_function(x1)): #swapping the functions only if function(x0) is less than the function(x1)
           x0, x1 = x1, x0 # swapping
        count += 1  #iteration counter starting
        x2 = x1 - original_function(x1) * (x0 - x1) / (original_function(x0) - original_function(x1)) #setting up x2
        x0 = x1 #setting x0 equal to x1
        x1 = x2 #setting x1 equal to x2
        if original_function(x2) == 0: #if function(x2) is 0 then the root is found
           root = x2 #setting x2 equal to the root
           return root, count #returning x2
        else:
           root = x1 #setting x1 equal to the root for more clarity
           if flag == "a":  # if the user choose to do absolute approximate error, continue
               err = abs(x0 - x1)  # setting the error to the value I get from |(x0-x1)|
               if err < tolerance:  #if the error is less than the user's tolerance return x1
                   return root, count  #returning x1 and counter after the previous changes
           elif flag == "b":  # if the user choose to do absolute relative approximate error, continue
               err = abs(x0 - x1) / abs(x1)  # setting the error to the value I get from |x0-x1| over |x1|
               if err < tolerance:  # if the error is less than the user's tolerance, continue
                   return root, count  # returning x1 and counter after the previous statements
           elif flag == "c":  # if the user choose to do the estimated true absolute error, continue
               err = abs(original_function(x1))  # setting the error equal to the value I get from |function(x1)|
               if err < tolerance:  # if the error is less than the user's tolerance, continue
                   return root, count  # returning x1 and counter after the previous lines of code
           elif flag == "d":  # if the user choose to do both absolute approximate & estimated true absolute error, continue
               err1 = abs(x0 - x1)  # set err1 equal to |(x0-x1)|
               err2 = abs(original_function(x0))  #set err2 equal to |function(x0)|
               if err1 < tolerance and err2 < tolerance:  #if both errors are less than the user's tolerance, continue
                   return root, count  #returning x1 and counter after previous actions