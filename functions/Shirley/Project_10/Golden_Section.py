# Importing symbols and diff functions from the sympy library for symbolic mathematics
from sympy import symbols, diff

# Function to perform the golden section search for finding minimum and maximum of a function
def golden_section(left_bracket, right_bracket, f, phi, delta):
    # Initialize variables a and b with the original interval boundaries
    a = left_bracket
    b = right_bracket
    # Calculate x1 and x2 using the golden ratio
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    # Evaluate the function at x1 and x2
    y1 = f(x1)  # f(x1)
    y2 = f(x2)  # f(x2)

    # Counter to track the number of iterations
    count = 0

    # First loop to find the minimum within the specified tolerance delta
    while abs(b - a) > delta:  # Continue until the interval is sufficiently small
        count += 1  # Increment iteration count
        if y1 >= y2:  # If y1 is greater, minimum is in the right subinterval
            a = x1  # Update the left boundary
            x1 = x2  # Move x2 closer to the minimum
            x2 = a + ((b - a) / phi)  # Compute new x2
            y1 = f(x1)  # Update y1
            y2 = f(x2)  # Update y2
        else:  # Otherwise, minimum is in the left subinterval
            b = x2  # Update the right boundary
            x2 = x1  # Move x1 closer to the minimum
            x1 = b - ((b - a) / phi)  # Compute new x1
            y1 = f(x1)  # Update y1
            y2 = f(x2)  # Update y2

        # Determine the minimum or maximum based on the flag
    if phi > 1:  # Finding maximum
        return (a + b) / 2, f((a + b) / 2), count
    else:  # Finding minimum
        return (a + b) / 2, f((a + b) / 2), count

    # Compute the estimated minimum point
    min = (a + b) / 2  # Midpoint of the interval

    # Reset the interval for finding the maximum
    a = left_bracket
    b = right_bracket
    x1 = b - ((b - a) / phi)
    x2 = a + ((b - a) / phi)
    y1 = f(x1)
    y2 = f(x2)

    # Second loop to find the maximum within the specified tolerance delta
    while abs(b - a) > delta:
        count += 1  # Increment iteration count
        if y1 <= y2:  # If y1 is smaller, maximum is in the right subinterval
            a = x1  # Update the left boundary
            x1 = x2  # Move x2 closer to the maximum
            x2 = a + ((b - a) / phi)  # Compute new x2
            y1 = f(x1)  # Update y1
            y2 = f(x2)  # Update y2
        else:  # Otherwise, maximum is in the left subinterval
            b = x2  # Update the right boundary
            x2 = x1  # Move x1 closer to the maximum
            x1 = b - ((b - a) / phi)  # Compute new x1
            y1 = f(x1)  # Update y1
            y2 = f(x2)  # Update y2

    # Compute the estimated maximum point
    max = (a + b) / 2  # Midpoint of the interval

    # Return results: minimum and maximum points, their function values, and iteration count
    return min, f(min), max, f(max), count