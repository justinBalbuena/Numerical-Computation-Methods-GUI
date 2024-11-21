#current test
x = [0.15, 0.21, .23,0.27, 0.32,0.35]
y = [.1761, .3222,.3617, .4314, .5051, .5441]

#extra credit test
#x = [0.15, .23, 0.32,0.35]
#y = [.1761, .3617, .5051, .5441]

# different tests
#x = [0.3,0.5,0.7,0.9,1.1]
#y = [0.404958,.824361,1.40963,2.21364,3.30458]

#from the slides
#x = [1.9,2.0,2.1,2.2]
#y = [12.703199,14.778112,17.148957,19.855030]

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


def numdef(x,y,h,flag,ty,wanted):
    #usern = float(input("Enter a number in which you wish to find the derivate for: "))
    usern = float(wanted)
    match ty:
        case 1:
            print("Interpolation type: Quadratic")
            utype = 3 #number of points we wish to include in the data set since quadratic is 3 we set = to 3

        case 2: #for cubic it is going to be 4 for 4 points
            print("Interpolation type: Cubic")
            utype = 4

    match flag:
        case 'a':
            counter = 0
            for i in range(1,len(x)): #what this function deos it selects where in the array we start based on what input the user entered
                if usern > x[i]: #this can likely be updated to work with a smaller array but for the sake of this project we won't
                    #in the line above we are simply checking if the users value is greater than the current value if its not then we break and return the value
                    counter += 1
                else:
                    break
            userx = [x[i] for i in range(counter, counter + utype)] #this is where we get the data set
            usery = [y[i] for i in range(counter,counter + utype)] #the second data set for the f(x) numbers
            print(userx)
            x0 = lagranged(usern,userx,usery)
            x1 = lagranged(usern+h,userx,usery)

            userdif = (x1 - x0)/h
            return f'The derivative at {usern} is: {userdif}'

        case 'b':
            counter = 0
            for i in range(1, len(x)):
                if usern > x[i]:
                    counter += 1
                else:
                    break

            userx = [x[i] for i in range(counter, counter + utype)]
            usery = [y[i] for i in range(counter, counter + utype)]

            x0 = lagranged(usern, userx, usery)
            x1 = lagranged(usern + h, userx, usery)
            x2 = lagranged(usern+(2*h),userx, usery)

            userdif = (1/(2*h)) * (-3*x0 + 4*x1 - x2)
            print()
            print(x0, x1, x2)
            print()
            return f'The derivative at {usern} is: {userdif}'
        case 'c':
            counter = 0
            for i in range(1, len(x)):
                if usern > x[i]:
                    counter += 1
                else:
                    break

            userx = [x[i] for i in range(counter, counter + utype)]
            usery = [y[i] for i in range(counter, counter + utype)]

            #x0 = lagranged(usern, userx, usery) we dont use this one here
            x1 = lagranged(usern + h, userx, usery)
            x2 = lagranged(usern - h, userx, usery) #this is the number behind the users value

            userdif = (1/(2*h)) * (x1 - x2)
            return f'The derivative at {usern} is: {userdif}'







