import sympy

def lagrange(val, x_arr, y_arr):  # Taking my lagrange from project 7
    interpolated_value = 0  # Initializing the result to 0
    n = len(x_arr) - 1  # Calculating the degree of the polynomial (number of data points minus one)
    for i in range(n + 1):  # Looping through each data point
        lagrangian = 1  # Initializing the Lagrange basis polynomial for the current term
        for j in range(n + 1):  # Looping through all data points to compute the Lagrange term
            if j != i:  # Skipping the current data point
                lagrangian *= (val - x_arr[j]) / (x_arr[i] - x_arr[j])  # Updating the Lagrange polynomial term
        interpolated_value += lagrangian * y_arr[i]  # Adding the contribution of the current term to the result
    return interpolated_value  # Returning the interpolated value

# Function to calculate derivative using Lagrange interpolation and finite difference
def lagrange_variation(val, x_arr, y_arr, selected_flag, h, interpolation_type="cubic"):
    # Sort x_arr and y_arr
    sorted_indices = sorted(range(len(x_arr)), key=lambda i: x_arr[i])
    x_arr = [x_arr[i] for i in sorted_indices]
    y_arr = [y_arr[i] for i in sorted_indices]

    # Validate data
    points_required = 3 if interpolation_type == "cubic" else 2
    if len(x_arr) < points_required:
        print(f"At least {points_required} data points are required for {interpolation_type} interpolation.")

    subset_x = x_arr[-points_required:]
    subset_y = y_arr[-points_required:]

    # Add interpolated values if needed
    if val not in x_arr:
        y_arr.append(lagrange(val, subset_x, subset_y))
        x_arr.append(val)

    if selected_flag in ['a', 'b'] and val + h not in x_arr:
        y_arr.append(lagrange(val + h, subset_x, subset_y))
        x_arr.append(val + h)

    if selected_flag == 'b' and val + 2 * h not in x_arr:
        y_arr.append(lagrange(val + 2 * h, subset_x, subset_y))
        x_arr.append(val + 2 * h)

    if selected_flag == 'c' and val - h not in x_arr:
        y_arr.append(lagrange(val - h, subset_x, subset_y))
        x_arr.append(val - h)

    # Calculate derivative
    if selected_flag == 'a':
        derivative = (y_arr[x_arr.index(val + h)] - y_arr[x_arr.index(val)]) / h
    elif selected_flag == 'b':
        derivative = (-y_arr[x_arr.index(val + 2 * h)] + 4 * y_arr[x_arr.index(val + h)] - 3 * y_arr[x_arr.index(val)]) / (2 * h)
    elif selected_flag == 'c':
        derivative = (y_arr[x_arr.index(val + h)] - y_arr[x_arr.index(val - h)]) / (2 * h)
    else:
        print("Invalid flag: Use 'a', 'b', or 'c'.")
    return derivative

# if __name__ == "__main__":  # Check if the script is run directly
#     print("Please enter the data points")  # Prompt the user for data points
#     x_arr = input("Ex: [0.15, 0.21, 0.23, 0.27, 0.32, 0.35]: ")  # Getting x values as a string
#     x_arr = eval(x_arr)  # Converts input string to list using eval
#     print("Please enter the function points")  # Prompt the user for function values
#     y_arr = input("Ex: [0.1761, 0.3222, 0.3617, 0.4314, 0.5051, 0.54410]: ")  # Getting y values as a string
#     y_arr = eval(y_arr)  # Converts input string to list using eval
#     val = float(input("Interpolate at \nEx: 0.26: "))  # Getting the interpolation point as a float
#     h = float(input("Please enter the step size \nEx: 0.01: "))  # Getting the step size as a float
#     print("a = 2-point forward difference formula\nb = 3-point forward difference formula\nc = 3-point centered difference formula")
#     for flag in ['a', 'b', 'c']:  # Iterating through different derivative calculation methods
#         derivative = lagrange_variation(val, x_arr, y_arr, flag, h, interpolation_type="cubic")  # Calculating the derivative
#         print(f"The derivative using method {flag} is {derivative}")