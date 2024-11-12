from sympy import symbols

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

x = symbols("x")

def trapezoidal_rule(x,f_x,h):
    sum_of_trapezoidal = 0
    for i in range(1,len(f_x)-1):
        x_k = i*h
        x_k += x[0]
        x_k = round(x_k,1)
        index = x.index(x_k)
        sum_of_trapezoidal += f_x[index]
    solution = h/2
    solution *= 2*sum_of_trapezoidal+f_x[0]+f_x[len(x)-1]
    return solution

def simpson_rule(x,f_x,h):
    sum_of_simpson1 = 0
    sum_of_simpson2 = 0
    e1 = int(8/2 - 1)
    e2 = int(8/2)
    for i in range(1,e1+1):
        x_k = x[0]
        x_k += 2*i*h
        x_k = round(x_k,1)
        index = x.index(x_k)
        sum_of_simpson1 += f_x[index]
    for i in range(1,e2+1):
        x_k = 2 * i - 1
        x_k *= h
        x_k += x[0]
        x_k = round(x_k,1)
        index = x.index(x_k)
        sum_of_simpson2 += f_x[index]

    x_n = h* 8
    x_n += x[0]
    index = x.index(x_n)
    solution = h/3
    solution *= f_x[0] + 2*sum_of_simpson1+ 4*sum_of_simpson2 + f_x[index]
    return solution


x = [1.0, 1.1, 1.3, 1.4, 1.5, 1.7, 1.8]
f_x = [1.543,1.669,1.971,2.151,2.352,2.828,3.107]
f_x1 = Lagrange(1.2,x=[1.0,1.1,1.3],f=[1.543,1.669,1.971])
f_x2 = Lagrange(1.6,x=[1.4, 1.5, 1.7],f=[2.151,2.352,2.828])
x.insert(2,1.2)
x.insert(6,1.6)
f_x.insert(2,f_x1)
f_x.insert(6,f_x2)
h = 0.1
print("Integrates continuous function using both trapezoidal and simpson rule")

solution = trapezoidal_rule(x,f_x,h)
solution1 = simpson_rule(x,f_x,h)
print("Trapezoidal rule: ", solution)
print("Simpson rule: ", solution1)
