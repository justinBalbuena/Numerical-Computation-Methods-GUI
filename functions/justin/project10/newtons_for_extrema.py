from sympy import *

def newtons_for_extrema(x0, tolerance, user_function):
    x_current = x0
    x_next = 0.0
    iterations = 0.0
    scaling_coefficient = 0.1

    # sets up a function using lambdify to set up the user's given function for usability
    x = symbols('x')
    user_function = user_function.replace('e', 'E')
    user_expression = sympify(user_function)
    # Create a callable function for the user's expression
    user_func = lambdify(x, user_expression)

    # Compute the derivative of the user's function
    derived_function = user_expression.diff(x)
    # Create a callable function for the derivative
    derivative_func = lambdify(x, derived_function)

    derived_function_second = derived_function.diff(x)
    derivative_func_second = lambdify(x, derived_function_second)

    while True:
        iterations += 1

        # Check if the second derivative is zero to avoid division by zero
        second_derivative_value = derivative_func_second(x_current)
        if second_derivative_value == 0:
            raise ValueError("Second derivative is zero at x = {x_current}. Cannot proceed.")

        # Newton's method formula for finding extrema
        x_next = x_current - scaling_coefficient * (derivative_func(x_current) / second_derivative_value)

        # Check if the change is within the tolerance
        if abs(x_next - x_current) <= tolerance:
            y_value = user_func(x_next)  # Compute the y-value at the extrema
            return x_next, y_value, iterations
        else:
            x_current = x_next


if __name__ == "__main__":
    while True:
        # Gets the equation from the user
        user_input = input("Enter a function of x in a python readable line (e.g., x**2 + 3), the sympy library is "
                           "imported so please use it as you'd like: ")

        # Gets the threshold value
        delta = float(input("Enter your threshold value: "))

        # Gets x0 value
        x0 = input("Please choose a starting value relatively close to the solution: ")

        results = newtons_for_extrema(float(x0), float(delta), user_input)
        print(f"The x value of the local extrema is: {results[0]}")
        print(f"The y value of the local extrema is: {results[1]}")
        print(f"The amount of iterations it took was: {results[2]}")


