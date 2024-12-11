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




def trapezoidal(h,x,y):
   length = len(x)
   a =1
   numsum = 0


   # here we find the sum of tabulated values and we start from the first index all the way to the second to last number
   for i in range(1,length-1):


       xindex = x.index(round(a+(h*i),1))
       numsum += y[xindex] #this


   numsum *= 2
   numsum += y[0] + y[-1]


   numsum *= h/2


   return numsum