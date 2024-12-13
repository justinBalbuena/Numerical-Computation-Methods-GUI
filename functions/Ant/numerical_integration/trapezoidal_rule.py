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