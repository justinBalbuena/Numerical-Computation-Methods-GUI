import math
from sympy import * #using this library for the function

def false_position_method(x0, x1, tolerance, flag, original_function):  #my false position function declaring the variables
   x = x1 #setting x equal to x1
   count = 0
   while True: #will run until it fits the one of the requirements
       count += 1  # iteration counter starting
       x2 = x1 - original_function(x1) * (x0 - x1) / (original_function(x0) - original_function(x1)) #setting up x2
       if (original_function(x0) * original_function(x2)) < 0: #if function(x0) times function(x2) is less than 0, set x1 = x2
           x1 = x2 #setting x1 equal to x2
       else:
           x0 = x2 #setting x0 equal to x2
       if original_function(x2) == 0: #if the function(x2) equals 0, then the root is found
           return x2, count #returning x2 and counter, with x2 being a root
       else:
           root = x2 #setting x2 as the root for more clarity
           if flag == "a":  #if the user choose to do absolute approximate error, continue
               err = abs(x - x2)  #setting the error to the value I get from |(x-x2)|
               if err < tolerance:  #if the error is less than the user's tolerance, continue
                   return root,count  #returning x2 and counter after the previous changes
               x = x2 #setting x equal to x2
           elif flag == "b":  # if the user choose to do absolute relative approximate error, continue
               err = abs(x - x2) / abs(x2)  # setting the error to the value I get from |x-x2| over |x2|
               if err < tolerance:  # if the error is less than the user's tolerance, continue
                   return root,count  #returning x2 and counter
               x = x2 #setting x equal to x2
           elif flag == "c":  # if the user choose to do the estimated true absolute error, continue
               err = abs(original_function(x2))  # setting the error equal to the value I get from |function(x2)|
               if err < tolerance:  # if the error is less than the user's tolerance, continue
                   return root,count  #returning x2 and counter
           elif flag == "d":  #if the user choose to do both absolute approximate & estimated true absolute error,continue
               err1 = abs(x - x2)  #set err1 equal to |(x-x2)|
               err2 = abs(original_function(x2))  #set err2 equal to |function(x2)|
               if err1 < tolerance and err2 < tolerance:  #if both errors are less than the user's tolerance, continue
                   return root,count  #returning x2 and counter
               x = x2 #setting x equal to x2