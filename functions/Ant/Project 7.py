def Lagrange(z, x, f):
    # Get the number of data points
    n = len(x)
    # Initialize the result of interpolation to 0
    interpolated_value =0.0
    # Loop over each data point to build the Lagrange polynomial
    for i in range(n-1):
        # Initialize the Lagrange basis polynomial to 1
        L = 1
        # Calculate the Lagrange basis polynomial for the current i
    for j in range(n-1):
        if j != i:
        # Multiply terms for basis polynomial excluding the i-th term
            L *= (z - x[j]) / (x[i] - x[j])
        # Accumulate the term for the current basis polynomial into the result
        interpolated_value += L * f[i]
        # Return the final interpolated value at point z
    return interpolated_value

inpop = float(input("Please enter a number: "))
x = [.3, .5, .7]
f = [.404958, .824361, 1.40963]
value = Lagrange(inpop,x,f)
print("Using only the first 3 data points")
print(value)
x =[.3,.5,.7,.9]
f = [.404958, .824361, 1.40963,2.21364]
value = Lagrange(inpop,x,f)
print("\nUsing only the first 4 data points")
print(value)
x =[.5,.7,.9,1.1]
f = [.824361, 1.40963,2.21364,3.30458]
value = Lagrange(inpop,x,f)
print("\nUsing only the last 4 data points")
print(value)
x = [.3, .5, .7, .9, 1.1]
f = [.404958, .824361, 1.40963,2.21364,3.30458]
value = Lagrange(inpop,x,f)
print("\nUsing only the given points data points")
print(value)