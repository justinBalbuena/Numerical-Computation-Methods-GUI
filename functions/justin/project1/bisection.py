import math
from sympy import *


def bisect(x1, x2, choice, user_function, delta):

    # sets up a function using lambdify to set up the user's given function for usability
    x = symbols('x')
    user_function = user_function.replace('e', 'E')
    user_expression = sympify(user_function)
    # Create a callable function for the user's expression
    user_func = lambdify(x, user_expression)

    # this ensures that valid brackets are chosen
    if user_func(x1) * user_func(x2) >= 0:
        while (user_func(x1) * user_func(x2)) >= 0:
            print("Please select values for x1 and x2 such that their multiplied value is negative")
            x1 = float(input("New Value for x1: "))
            x2 = float(input("New Value for x2: "))

    # setting up variables for use
    iteration = 0
    x3 = 0.0
    x4 = 0.0
    epsilon = 100.0

    # this begins the iterative process
    while True:
        iteration = iteration + 1
        x3 = (x1 + x2) / 2
        if user_func(x3) == 0:
            root = x3
            return root, iteration
        else:
            # narrows the interval
            if user_func(x1) * user_func(x3) < 0:
                x2 = x3
                x4 = x1
            else:
                x1 = x3
                x4 = x2

            match choice:
                # compares using the absolute approximate error
                case 'a':
                    epsilon = math.fabs(x1 - x2)
                    if epsilon < delta:
                        return x3, iteration
                # compares using the absolute relative approximate error
                case 'b':
                    epsilon = math.fabs(x3 - x4) / math.fabs(x3)
                    if epsilon < delta:
                        return x3, iteration
                # compares using the true absolute error
                case 'c':
                    epsilon = math.fabs(user_func(x3))
                    if epsilon < delta:
                        return x3, iteration
                # compares using a Conjunction of an absolute approximate error and an estimated true absolute error
                case 'd':
                    if math.fabs(x1 - x2) < delta and math.fabs(user_func(x3)) < delta:
                        return x3, iteration

if __name__ == "__main__":
    while True:
        # Gets the equation from the user
        user_input = input("Enter a function of x in a python readable line (e.g., x**2 + 3): ")

        # Gets the bounds
        left_bound = float(input("Enter your left bound value: "))
        right_bound = float(input("Enter your right bound value: "))

        # Gets the stopping criteria
        stopping_criteria = input("Enter 'absolute_approximate', 'absolute_relative', 'true_absolute_error', 'conjunction' "
                                  "for the stopping criteria that you want ")
        delta = float(input("Enter your threshold value: "))
        match stopping_criteria:
            case 'absolute_approximate':
                print("Value, Iterations")
                print(bisect(left_bound, right_bound, stopping_criteria, user_input, delta))
                print("\n")
            case 'absolute_relative':
                print("Value, Iterations")
                print(bisect(left_bound, right_bound, stopping_criteria, user_input, delta))
                print("\n")
            case 'true_absolute_error':
                print("Value, Iterations")
                print(bisect(left_bound, right_bound, stopping_criteria, user_input, delta))
                print("\n")
            case 'conjunction':
                print("Value, Iterations")
                print(bisect(left_bound, right_bound, stopping_criteria, user_input, delta))
