def simpson_rule(x,f_x,h):
    #variable the holds value for Σ
    n=len(x)-1
    if n % 2 == 0:
        return 0
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
    #finds the index in x where
    index = x.index(x_n)
    #equations for the solution
    solution = h/3
    solution *= f_x[0] + 2*sum_of_simpson1+ 4*sum_of_simpson2 + f_x[index]
    return solution