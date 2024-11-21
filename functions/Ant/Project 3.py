from sympy import *

# Define the Newton-Raphson method function
def newton(x0, function, tolerance, flag):
    i = 0  # Initialize iteration counter
    while True:
        # Check if the current function value is zero (exact root found)
        if function(x0).evalf() == 0:
            return x0, i  # Return the root and number of iterations
        else:
            i += 1  # Increment iteration count
            # Creates a lambda function that utilises the derivative of the function entered
            function_dx = lambdify(x, diff(function(x)))

            # Check if the derivative is zero to avoid division by zero
            if function_dx(x0) == 0:
                new_x0 = input("Please enter new number near the root!: ")
                x0 = eval(new_x0)  # Get new approximation from user input
            else:
                # Apply Newton's method formula to find next approximation
                # Utilises  evalf() to obtain a value from the lambda function not need if using math

                x1 = x0 - function(x0).evalf() / function_dx(x0)

                # Determine the error based on the selected flag
                match flag:
                    case "a":  # Absolute approximate error
                        error = abs(x0 - x1)
                        if error < tolerance:  # Check if error is within tolerance
                            return x1, i  # Return root and iterations
                        else:
                            x0 = float(x1)  # Update x0 for next iteration, creates issues because x1 is a type sympy float
                    case "b":  # Absolute relative approximate error
                        error = abs(x1 - x0) / abs(x1)
                        if error < tolerance:
                            return x1, i
                        else:
                            x0 = float(x1)
                    case "c":  # True absolute error
                        error = abs(function(x0))
                        if error < tolerance:
                            return x1, i
                        else:
                            x0 = float(x1)
                    case "d":  # Combined error criteria
                        error = abs(x1 - x0)
                        error1 = abs(x1 - x0) / abs(x1)
                        if  error1 < tolerance or error < tolerance:
                            return x1, i
                        else:
                            x0 = float(x1)

# Define symbolic variable
x = symbols('x')
# Get user-defined function as input
user_function = input("Write function: ")
tolerance = 10 ** -6  # Set tolerance level
# Display options for stopping criteria
print("a) An absolute approximate error is used to stop the process.\n")
print("b) An absolute relative approximate error is used to stop the process.\n")
print("c) Estimation of a true absolute error is used to stop the process.\n")
print("d) Conjunction of an absolute approximate error and an estimated true absolute error is used to stop the process \n")

# Get user's choice of stopping criteria and initial guess
user_flag = input("What method do you choose to find root?: ")
user_x0 = eval(input("Please type a number close to root: "))
function = lambda x: eval(user_function)  # Create a lambda function for user input

# Call the Newton method and print results
roots, iteration = newton(user_x0, function, tolerance, user_flag)
print("Roots: ", roots, " Iterations", iteration)  # Output found root and iterations
