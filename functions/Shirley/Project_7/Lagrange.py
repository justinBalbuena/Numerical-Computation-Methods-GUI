def lagrange(z, x, f):
    interpolated_value = 0  # initialize interpolated value to 0
    n = len(x) - 1  # number of data points - 1
    for i in range(n + 1):  # iterate over each data point
        lagrangian = 1  # initialize Lagrangian
        for j in range(n + 1):  # iterate through all data points
            if j != i:  # skip the current point
                lagrangian = lagrangian * (z - x[j]) / (x[i] - x[j])  # calculate Lagrange multiplier
        interpolated_value = interpolated_value + lagrangian * f[i]  # add the weighted value to the total
    return interpolated_value

# print("Please enter the data points")
# x = input("Ex: [0.3, 0.5, 0.7]: ")  #getting x values
# x = eval(x)  #converts input string to list
# print("Please enter the function points")
# f = input("Ex: [0.404958, 0.824361, 1.40963]: ")  #getting f(x) values
# f = eval(f)  #converts input string to list
# z = float(input("Interpolate at \nEx: 0.6: "))  #getting the  interpolation point
# interpolated_value = lagrange(z, x, f) #calling the function
# print("Interpolated value is", interpolated_value) #printing the function