import math

def trapezoidal_rule (h, fx): #creating my trapezoidal rule function
    x_values = sorted(fx.keys())
    y_values = [fx[x] for x in x_values]
    n_intervals = int((x_values[-1] - x_values[0]) / h)  # Number of intervals
    interpolated_x = [x_values[0] + i * h for i in range(n_intervals + 1)]  # Uniformly spaced x-values
    interpolated_y = []
    for x in interpolated_x:
        if x in fx:
            interpolated_y.append(fx[x])  # Use existing value if x is in original data
        else:
            # Interpolate using Lagrange for missing points
            interpolated_y.append(lagrange(x, x_values, y_values))

    integral = 0 #initializing my integral
    for i in range (len(interpolated_x)- 1): #running through intervals until the second to last one
        integral += h * ((interpolated_y[i]+ interpolated_y[i+1]) / 2) #using the formula taken from the lecture notes
    return integral #returning the integral

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