# Importing symbols and diff functions from the sympy library for symbolic mathematics
from sympy import symbols, diff

# Function to perform Newton's method for finding roots or extrema of a function
def newtons_method(x, f, delta, scalingcoeff):
    # Define a symbolic variable 'var'
    var = symbols('var')
    # Counter to track the number of iterations
    count = 0
    # Iterative loop for Newton's method
    while True:
        count = count + 1  # Increment iteration count
        # Compute the next approximation using Newton's method formula
        newx = x - scalingcoeff * ((diff(f, var)).subs(var, x)) / ((diff(f, var, 2)).subs(var, x))
        # Evaluate the function at the new approximation
        fnewx = f.subs(var, newx)
        # Check if the change is within the specified tolerance delta
        if abs(newx - x) <= delta:
            return newx, fnewx, count  # Return results: root/extremum, function value, and iteration count
        else:
            # Slightly adjust 'x' if not yet converged
            x = x + 0.01
