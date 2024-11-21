from math import *


# def bisection_method(x1, x2, function, tolerance, flag):
#     function = lambda x: eval(function)
#     i = 0  # Initialize iteration counter
#     # Check if the initial brackets enclose a root
#     if function(x1) * function(x2) > 0:
#         print("Brackets do not intersect a root!")
#         x1 = input("Please enter a new x1: ")  # Prompt for new x1
#         x2 = input("Please enter a new x2: ")  # Prompt for new x2
#     else:
#         while True:
#             i += 1  # Increment iteration counter
#             x3 = (x1 + x2) / 2  # Calculate midpoint
#
#             # Check if the midpoint is a root
#             if function(x3) == 0:
#                 return x3, i  # Return the root and number of iterations
#
#             # Determine the next interval
#             if function(x1) * function(x3) < 0:
#                 x2, x4 = x3, x1  # Root lies between x1 and x3
#             else:
#                 x1, x4 = x3, x2  # Root lies between x3 and x2
#
#             # Determine stopping criteria based on user choice
#             match flag:
#                 case "a":
#                     error = abs(x3 - x4)  # Absolute error
#                     if error < tolerance:
#                         return x3, i  # Return if within tolerance
#                 case "b":
#                     error = abs(x3 - x4) / abs(x3)  # Relative error
#                     if error < tolerance:
#                         return x3, i  # Return if within tolerance
#                 case "c":
#                     error = abs(function(x3))  # Estimated true error
#                     if error < tolerance:
#                         return x3, i  # Return if within tolerance
#                 case "d":
#                     error = abs(x3 - x4)  # Absolute error
#                     error1 = abs(x3 - x4) / abs(x3)  # Relative error
#                     if error < tolerance and error1 < tolerance:
#                         return x3, i  # Return if either error is within tolerance
#

# Get user-defined function and parameters
# user_function = input("What is your nonlinear function? (use x, sin, pi): \n")
# function = lambda x: eval(user_function)  # Create function from user input
# tolerance = 10 ** -6  # Set tolerance level
#
# # Display stopping criteria options to the user
# print("a) An absolute approximate error is used to stop the process.\n")
# print("b) An absolute relative approximate error is used to stop the process.\n")
# print("c) Estimation of a true absolute error is used to stop the process.\n")
# print(
#     "d) Conjunction of an absolute approximate error and an estimated true absolute error is used to stop the process \n")
#
# user_flag = input("How do you wish to stop: ")  # Get stopping criteria choice
# user_x1 = input("Please enter a x1: ")  # Get initial x1
# user_x2 = input("Please enter a x2: ")  # Get initial x2
#
# # Call the bisection method and print results
# roots, iteration = bisection_method(eval(user_x1), eval(user_x2), function, tolerance, user_flag)
# print("Roots: ", roots, "Iteration: ", iteration)
