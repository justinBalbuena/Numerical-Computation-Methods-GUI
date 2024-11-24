def secant_method(x0, x1, tolerance, flag, function):
    """Perform the Secant Method to find the root of a function."""
    function_x0 = function(x0)  # Evaluate function at x0
    function_x1 = function(x1)  # Evaluate function at x1
    i = 0  # Iteration counter

    # Ensure x0 has the greater function value
    if abs(function_x0) < abs(function_x1):
        x0, x1 = x1, x0

    while True:
        i += 1  # Increment iteration count
        # Compute the next approximation using the formula
        x2 = x1 - function_x1 * (x0 - x1) / (function_x0 - function_x1)
        x0, x1 = x1, x2  # Update x0 and x1

        if function(x2) == 0:  # Check if root is found
            return x2 # Return root and iteration count

        # Determine stopping criteria based on the selected flag
        if flag == "a":  # Absolute error
            error = abs(x0 - x1)
            if error < tolerance:
                return x1
        if flag == "b":  # Relative error
            error = abs(x1 - x0) / abs(x1)
            if error < tolerance:
                return x1
        if flag == "c":  # True error estimation
            error = abs(function(x0))
            if error < tolerance:
                return x1
        if flag == "d":  # Conjunction of absolute and true errors
            error = abs(x0 - x1)
            error1 = abs(x1 - x0) / abs(x1)
            if error < tolerance or error1 < tolerance:
                return x1