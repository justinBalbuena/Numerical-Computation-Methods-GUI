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

def trapezoidal_rule(x,f_x,h):
    # creates variable to store the answer for Σ
    sum_of_trapezoidal = 0
    for i in range(1,len(f_x)-1):
        #separated the equations so the math doesn't collide
        x_k = i*h
        x_k += x[0]
        #round due to python incorrect arithmetic
        x_k = round(x_k,1)
        #find the value of x and match it to f_x table
        index = x.index(x_k)
        sum_of_trapezoidal += f_x[index]
    #same as last time simplify the math
    solution = h/2
    solution *= 2*sum_of_trapezoidal+f_x[0]+f_x[len(x)-1]
    return solution

def simpson_rule(x,f_x,h):
    #variable the holds value for Σ
    n = len(x)-1
    sum_of_simpson1 = 0
    sum_of_simpson2 = 0
    #creates variables that will determine the range for both Σ limit
    e1 = int(n/2 - 1)
    e2 = int(n/2)
    for i in range(1,e1+1):
        #same as before
        x_k = x[0]
        x_k += 2*i*h
        #rounds again to fix python math error
        x_k = round(x_k,1)
        #value found in x will match it to f_x
        index = x.index(x_k)
        sum_of_simpson1 += f_x[index]
    for i in range(1,e2+1):
        # same as before
        x_k = 2 * i - 1
        x_k *= h
        x_k += x[0]
        # rounds again to fix python math error
        x_k = round(x_k,1)
        # value found in x will match it to f_x
        index = x.index(x_k)
        sum_of_simpson2 += f_x[index]
    #equation to determine x_n
    x_n = h*n
    x_n += x[0]
    print(x_n)
    #finds the index in x where
    index = x.index(x_n)
    #equations for the solution
    solution = h/3
    solution *= f_x[0] + 2*sum_of_simpson1+ 4*sum_of_simpson2 + f_x[index]
    return solution
def main():
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
main()
