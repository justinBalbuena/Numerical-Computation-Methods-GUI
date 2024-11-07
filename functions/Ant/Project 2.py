import random
from math import *
def value_x1(x0, function):
    """Generate a second approximation (x1) based on x0."""
    x1 = x0 + 1 # Initial guess for x1
    if function(x0) < function(x1): # Check if the function decreases
        x1 = x0 - 1 # Adjust x1 if necessary
        return x1
def FP_value_x1(x0, function):
    x1 = random.uniform(x0 - 10, x0 + 10) # Random initial guess for x1
    for i in range(100): # Limit attempts to find a valid x1
        if function(x0) * function(x1) > 0: # Check if signs are the same
            x1 = random.uniform(x0 - 0.5, x0 + 0.5) # Generate new x1 if signs are the same
        else:
            break
        if function(x0) * function(x1) < 0:
            return x1 # Return valid x1 if found
        else:
            print("Bracket could not be found") # Indicate failure to find a valid x1
def secant_method(x0, x1, tolerance, flag, function):
    function_x0 = function(x0) # Evaluate function at x0
    function_x1 = function(x1) # Evaluate function at x1
    i = 0 # Iteration counter
    # Ensure x0 has the greater function value
    if function_x0 < abs(function_x1):
        x0, x1 = x1, x0
    while True:
        i += 1 # Increment iteration count
        # Compute the next approximation using the formula
        x2 = x1 - function(x1) * (x0 - x1) / (function(x0) - function(x1))
        x0, x1 = x1, x2 # Update x0 and x1
        if function(x2) == 0: # Check if root is found
            return x2, i # Return root and iteration count
        # Determine stopping criteria based on the selected flag
        if flag == "a": # Absolute error
            error = abs(x0 - x1)
            if error < tolerance:
                return x2, i  # Return root and iteration count
        if flag == "b":  # Relative error
            error = abs(x1 - x0) / abs(x1)
            if error < tolerance:
                return x1, i
        if flag == "c":  # True error estimation
            error = abs(function(x0))
            if error < tolerance:
                return x1, i
        if flag == "d":  # Conjunction of absolute and true errors
            error = abs(x0 - x1)
            error1 = abs(x1 - x0) / abs(x1)
            if error < tolerance or error1 < tolerance:
                return x1, i
def falsePosition_method(x0, x1, tolerance, flag, function):
    """Perform the False Position Method to find the root of a function."""
    x3 = x1 # Store previous approximation for error calculation
    i = 0 # Iteration counter
    while True:
        i += 1 # Increment iteration count
        # Compute the next approximation using the False Position formula
        x2 = x1 - function(x1) * (x0 - x1) / (function(x0) - function(x1))
        if function(x2) == 0: # Check if root is found
            return x2, i # Return root and iteration count
        else:
            # Update the interval based on the function values
            if function(x0) * function(x1) < 0:
                x1 = x2 # Keep x2 as the new upper bound
            else:
                x0 = x2 # Keep x2 as the new lower bound
        # Determine stopping criteria based on the selected flag
        if flag == "a":  # Absolute error
            error = abs(x3 - x2)
            if error < tolerance:
                return x2, i
            else:
                x3 = x2  # Update previous approximation
        if flag == "b":  # Relative error
            error = abs(x3 - x2) / abs(x2)
            if error < tolerance:
                return x2, i
            else:
                x3 = x2  # Update previous approximation
        if flag == "c":  # True error estimation
            error = abs(function(x2))
            if error < tolerance:
                return x2, i
            else:
                x3 = x2  # Update previous approximation
        if flag == "d":  # Conjunction of absolute and true errors
            error = abs(x3 - x2)
            error1 = abs(x3 - x2) / abs(x2)
            if error < tolerance or error1 < tolerance:
                return x2, i
            else:
                x3 = x2  # Update previous approximation
# User input for function and method selection
user_function = input("Write function: ")
function = lambda x: eval(user_function) # Create a lambda function from user input
tolerance = 10 **-6 # Set tolerance for stopping criteria
# Display available stopping criteria
print("a) An absolute approximate error is used to stop the process.\n")
print("b) An absolute relative approximate error is used to stop the process.\n")
print("c) Estimation of a true absolute error is used to stop the process.\n")
print("d) Conjunction of an absolute approximate error and an estimated true absolute error is used to stop the process \n")
# User input for stopping criterion
user_flag = input("What approach do you choose?: ")
print("1. Secant method \n2. False Position")
user_method = input("What method do you choose to find root?: ")
# Execute the chosen method
if user_method == "1":
    user_x0 = input("Please type a number for x0: ")
    user_x1 = value_x1(eval(user_x0), function) # Get x1 based on x0
    roots, iterations = secant_method(eval(user_x0), user_x1, tolerance, user_flag, function)
    print("Roots: ", roots," Iterations: ", iterations)
if user_method == "2":
    user_x0 = input("Please type a number for x0: ")
    user_x1 = FP_value_x1(eval(user_x0), function) # Get x1 for the False Position Method
    roots, iterations = falsePosition_method(eval(user_x0), user_x1, tolerance, user_flag,function)
    print("Roots: ", roots," Iterations: ", iterations)