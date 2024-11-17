from numpy import *
from scipy.optimize import fsolve

def ant_bisection_method(x1, x2,user_function, tolerance, flag):
    function = lambda x: eval(user_function)
    i = 0  # Initialize iteration counter
    # Check if the initial brackets enclose a root
    if function(x1) * function(x2) > 0:
        print("Brackets do not intersect a root!")
        x1 = input("Please enter a new x1: ")  # Prompt for new x1
        x2 = input("Please enter a new x2: ")  # Prompt for new x2
    else:
        while True:
            i += 1  # Increment iteration counter
            x3 = (x1 + x2) / 2  # Calculate midpoint

            # Check if the midpoint is a root
            if function(x3) == 0:
                return x3, i  # Return the root and number of iterations

            # Determine the next interval
            if function(x1) * function(x3) < 0:
                x2, x4 = x3, x1  # Root lies between x1 and x3
            else:
                x1, x4 = x3, x2  # Root lies between x3 and x2

            # Determine stopping criteria based on user choice
            match flag:
                case "a":
                    error = abs(x3 - x4)  # Absolute error
                    if error < tolerance:
                        return x3, i  # Return if within tolerance
                case "b":
                    error = abs(x3 - x4) / abs(x3)  # Relative error
                    if error < tolerance:
                        return x3, i  # Return if within tolerance
                case "c":
                    error = abs(function(x3))  # Estimated true error
                    if error < tolerance:
                        return x3, i  # Return if within tolerance
                case "d":
                    error = abs(x3 - x4)  # Absolute error
                    error1 = abs(x3 - x4) / abs(x3)  # Relative error
                    if error < tolerance and error1 < tolerance:
                        return x3, i  # Return if either error is within tolerance
def find_roots(user_function,x0):
    return fsolve(user_function,x0)
# def absolute_error_method():
#     return "a"
# def relative_error_method():
#     return "b"
# def true_absolute_error_method():
#     return "c"
# def combination():
#     return "d"
# error_tolerance_methods = {
#     #"Absolute Error": absolute_error_method,
#     "Relative Error": relative_error_method,
#     "True Absolute Error": true_absolute_error_method,
#     "Combination of Absolute Error and Relative Error": combination
# }
# def main():
#     error_method = st.radio("Error Tolerance Method", error_tolerance_methods.keys())
#     result = error_tolerance_methods[error_method]()
#

# main()

def main():
    fun = "sin(x)+cos(x)"
    function = lambda x: eval(fun)
    sol1,i = ant_bisection_method(-5,-3,"sin(x)+cos(x)",10**-6,"a")
    sol2 = find_roots(function,-5)

    print(sol1,sol2[0])
main()