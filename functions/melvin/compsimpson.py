def lagranged(x1,x,y):

    m = len(x) #here we get the length of the array
    n = m-1
    userx = x1 #take the users value
    insum = 0 #initialize the the sum value

    for i in range(n+1):
        l = 1 #here is where the lagrange value is initialized

        for j in range(n+1):

            if i != j:
                l *= (userx - x[j])/(x[i] - x[j]) # here is where we perform the interpolation calculatoins
                # we mutltiply the current lagrangian value by the current value divided by x[i] where its
                #not equal to j


        insum += y[i] * l

    return insum


def composimp(h,x,y):
    #h here being the segment size
    # x and y are arrays of values
    length = len(x) # length of array
    a =1
    numsum = 0
    numsum2 = 0

    # here we find the sum of tabulated values and we start from the first index all the way to the second to last number
    for i in range(1,int((length/2))): # This is the length of the array divided by 2 and then subtracted by 1
        xindex = x.index(round(a+(h*(2*i)),1)) # finding the index we need to go to in the y array
        numsum += y[xindex] #this

    for i in range(1,int(length/2)+1): # here we find the numbers that are odd values ad multiply them by 4
        xindex = x.index(round(a+(h*((2*i)-1)),1))
        numsum2 += y[xindex] #this


    numsum *= 2 # first loop
    numsum2 *= 4 # second loop

    #y[-1] is actually b in this case
    numsum += y[0] + y[-1] + numsum2

    numsum *= h/3

    return numsum


