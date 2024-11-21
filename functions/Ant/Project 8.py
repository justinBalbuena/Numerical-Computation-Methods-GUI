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


def PtsFwdAndCenter(value_x, x, f, h, flag, type_f):
    n = len(x)
    temp = x.copy()
    temp_f = f.copy()
    less = 0
    greater = 0
    for i in range(n):
        if temp[i] > value_x:
            greater += 1
        else:
            less += 1
    if n > 4 and type_f == "Quadratic":
        type_f = "Cubic"
    if n < 3 and type_f == "Cubic":
        type_f = "Quadratic"
    if type_f == "Quadratic":
        while n > 3:
            if less > greater:
                temp.pop(0)
                less -= 1
            else:
                temp.pop()
                greater -= 1
            n = len(temp)

    if type_f == "Cubic":
        while n > 4:
            if less > greater:
                temp.pop(0)
                temp_f.pop(0)
                less -= 1
            else:
                temp.pop()
                temp_f.pop()
                greater -= 1
            n = len(temp)

    match flag:
        case "a":
            answer = Lagrange(value_x + h, temp, temp_f) - Lagrange(value_x, temp, temp_f)
            answer /= h
            return answer
        case "b":
            answer = (-1 * Lagrange(value_x + 2 * h, temp, temp_f) + 4 * Lagrange(value_x + h, temp,
                                                                                  temp_f) - 3 * Lagrange(value_x, temp,
                                                                                                         temp_f))
            answer /= 2 * h
            return answer
        case "c":
            answer = Lagrange(value_x + h, temp, temp_f) - Lagrange(value_x - h, temp, temp_f)
            answer /= 2 * h
            return answer


# inpop = float(input("Please enter a number: "))
inpop = .26
x = [.15, .23, .32, .35]
f = [.1761, .3617, .5051, .5441]

# x = [.3, .5, .7, .9, 1.1]
# f = [.404958, .824361, 1.40963,2.21364,3.30458]
# x = [1.9,2.0,2.1,2.2]
# f = [12.703199,14.778112,17.148957,19.855030]
h = .01

answer = PtsFwdAndCenter(inpop, x, f, h, "a", type_f="Quadratic")
print("Method A: ")
print(answer)

answer = PtsFwdAndCenter(inpop, x, f, h, "b", type_f="Quadratic")
print("Method B: ")
print(answer)

answer = PtsFwdAndCenter(inpop, x, f, h, "c", type_f="Quadratic")
print("Method C: ")
print(answer)
