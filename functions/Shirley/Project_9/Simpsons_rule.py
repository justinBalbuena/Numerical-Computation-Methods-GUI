def simpsons_rule (h, fx): #creating the simpsons rule function
    # Convert dictionary to sorted lists
    x_values = sorted(fx.keys())
    y_values = [fx[x] for x in x_values]
    # Ensure equal spacing for x_values using Lagrange interpolation
    n_intervals = int((x_values[-1] - x_values[0]) / h)  # Number of intervals
    interpolated_x = [x_values[0] + i * h for i in range(n_intervals + 1)]  # Uniformly spaced x-values
    interpolated_y = []
    for x in interpolated_x:
        if x in fx:
            interpolated_y.append(fx[x])  # Use existing value if x is in original data
        else:
            # Interpolate using Lagrange for missing points
            interpolated_y.append(lagrange(x, x_values, y_values))
    # Apply Simpson's rule
    integral = interpolated_y[0] + interpolated_y[-1]  # f(a) + f(b)
    n = len(interpolated_x) - 1  # Number of sub-intervals
    for k in range (1, n, 2): #looping through the odd terms
        integral += 4 * fx[1][k] #multiplying the terms by 4 and adding it to the integral
    for k in range (2, n, 2): #looping through the even terms
        integral += 2 * fx[1][k] #multiplying the terms by 2 and adding it to the integral
    integral += fx[1][-1] #adding the last term f(b)
    integral *= (h/3) #multiplying the sum by h/3
    return integral #returning the updated integral

def lagrange(z, x, f):
    interpolated_value = 0  #initialize the interpolated value to zero
    n = len(x) - 1  #the number of data points subtracted by 1
    for i in range(n + 1):  #iterating through each data point
        lagrangian = 1  #initialize lagrangian
        for j in range(n + 1):  #iterate through all data points
            if j != i:  #skipping the current point
                lagrangian *= (z - x[j]) / (x[i] - x[j])  #calculating the lagrangian
        interpolated_value += lagrangian * f[i]  #changing the interpolated value
    return interpolated_value #returning the value