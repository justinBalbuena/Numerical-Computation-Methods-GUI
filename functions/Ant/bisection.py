from numpy import *

def ant_bisection_method(x1, x2,user_function, tolerance, flag):
    function = lambda x: eval(user_function)
    i = 0  # Initialize iteration counter
    # Check if the initial brackets enclose a root
    if function(x1) * function(x2) > 0:
        return False
    else:
        while True:
            i += 1  # Increment iteration counter
            x3 = (x1 + x2) / 2  # Calculate midpoint

            # Check if the midpoint is a root
            if function(x3) == 0:
                return x3, i  # Return the root and number of iterations

            # Determine the next interval
            if function(x1) * function(x3) < 0:
                x2, x4 = x3, x1  # Root lies between x1 and x3
            else:
                x1, x4 = x3, x2  # Root lies between x3 and x2

            # Determine stopping criteria based on user choice
            match flag:
                case "a":
                    error = abs(x3 - x4)  # Absolute error
                    if error < tolerance:
                        return x3 # Return if within tolerance
                case "b":
                    error = abs(x3 - x4) / abs(x3)  # Relative error
                    if error < tolerance:
                        return x3  # Return if within tolerance
                case "c":
                    error = abs(function(x3))  # Estimated true error
                    if error < tolerance:
                        return x3 # Return if within tolerance
                case "d":
                    error = abs(x3 - x4)  # Absolute error
                    error1 = abs(x3 - x4) / abs(x3)  # Relative error
                    if error < tolerance and error1 < tolerance:
                        return x3  # Return if either error is within tolerance

