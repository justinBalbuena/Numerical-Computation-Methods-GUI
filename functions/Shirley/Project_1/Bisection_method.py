import math
from sympy import *
def bisection_method(x1,x2, function, tolerance, flag): #my bisection function declaring the
   #x1, x2, tolerance, flag, and the function
   x = symbols('x')  # x is an unknown value
   original_function = lambdify(x, function) #taking in the user function as a lambda function
   x3 = (x1+x2)/2 #interval halving x3
   #count = 0 #iteration counter set to zero
   while original_function(x3) != 0: #in order to evaluate f(x3) I set up a while loop for all the cases I'll make
       #count += 1 #iteration counter starting
       val = original_function(x1) * original_function(x3) #setting up the value for the first two cases
       if val < 0: #narrowing the interval by using the value that we got from function(x1)*function(x2)
           x2 = x3 #setting x2 equal to x3
           x4 = x1 #setting x4 equal to x1
       else: #if val is greater than 0
           x1 = x3 #set x1 equal to x3
           x4 = x2 #set x4 equal to x2
       if flag == "a": #if the user choose to do absolute approximate error, continue
           err = abs(x3-x4) #setting the error to the value we get from |(x3-x4)|
           if err < tolerance: #if the error is less than the user's tolerance return x3
               return x3 #return x3 and counter after the previous changes
       elif flag == "b": #if the user choose to do absolute relative approximate error, continue
           err = abs(x3-x4)/abs(x3) #setting the error to the value we get from |x3-x4|over|x3|
           if err < tolerance: #if the error is less than the user's tolerance, continue
               return x3 #return x3 after the previous statements
       elif flag == "c": #if the user choose to do the estimated true absolute error, continue
           err = abs(original_function(x3)) #setting the error equal to the value we get from |function(x3)|
           if err < tolerance: #if the error is less than the user's tolerance, continue
               return x3 #return x3 after previous lines of code
       elif flag == "d": #if the user choose to do both absolute approximate & estimated true absolute error,continue
           err1 = abs(x3-x4) #set err1 equal to |(x3-x4)|
           err2 = abs(original_function(x3)) #set err2 equal to |function(x3)|
           if err1 < tolerance and err2 < tolerance: #if both errors are less than the user's tolerance, continue
               return x3 #return x3 after previous actions
       x3 = (x1 + x2) / 2 #keep halving until it fits the requirements
   return x3 #returning x3 as a new value