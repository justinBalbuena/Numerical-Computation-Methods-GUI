import random
from math import *

def ant_FP_value_x1(x0, user_function):
    """Generate a random x1 such that f(x0) and f(x1) have opposite signs."""
    x1 = random.uniform(x0 - 10, x0 + 10)  # Random initial guess for x1
    function = lambda x: eval(user_function)
    for i in range(100):  # Limit attempts to find a valid x1
        if function(x0) * function(x1) > 0:  # Check if signs are the same
            x1 = random.uniform(x0 - 0.5, x0 + 0.5)  # Generate new x1 if signs are the same
        else:
            break
    if function(x0) * function(x1) < 0:
        return x1  # Return valid x1 if found
    else:
        return 0# Indicate failure to find a valid x1

def ant_falsePosition_method(x0, x1, tolerance, flag, user_function):
    x3 = x1 # Store previous approximation for error calculation
    i = 0 # Iteration counter
    function = lambda x: eval(user_function)
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