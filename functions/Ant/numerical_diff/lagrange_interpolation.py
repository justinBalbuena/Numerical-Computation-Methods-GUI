def Lagrange(z, x, f):
    # Get the number of data points
    n = len(x)
    # Initialize the result of interpolation to 0
    interpolated_value = 0.0
    # Loop over each data point to build the Lagrange polynomial
    for i in range(n):
        # Initialize the Lagrange basis polynomial to 1
        L = 1
        # Calculate the Lagrange basis polynomial for the current i
        for j in range(n):
            if j != i:
                L *= (z - x[j]) / (x[i] - x[j])
        interpolated_value += L * f[i]
    return interpolated_value
