import streamlit as st
from sympy import * #using this library for the derivative function

def Newtons_Method(x0, tolerance, flag, function): #my Newton function declaring the variables I'll use
    count = 0 #iteration counter set to zero
    x0 = float(x0)
    x = symbols('x')
    original_function = lambdify(x, sympify(function))
    f_prime_sym = diff(sympify(function), x)
    f_prime = lambdify(x, f_prime_sym)
    while True: #will run until it fits the one of the requirements
        if original_function(x0) == 0: #if the users function(x0) equals 0, return1
            return
        if f_prime(x0) == 0: #if f_prime(x0) equals 0, continue
             #x0 = float(input("Please choose another x0: ")) #taking in my x0d until it mets the conditions
            continue
        count += 1 #iteration counter set
        x1 = x0 - (original_function(x0)/f_prime(x0)) #setting x1 equal to x0 - (user's function(x0) over fprime(x0))
        if original_function(x1) == 0: #if the user's function(x1) equals 0, continue
            root = x1 #setting root equal to x1
            return root, count #return the x1 and counter
        else:
            root = x1  #setting x1 equal to the root for more clarity
            if flag == "a": #if the user choose to do absolute approximate error, continue
                err = abs(x0-x1) #setting the error to the value we get from |(x3-x4)|
                if err < tolerance: #if the error is less than the user's tolerance return x3
                    return root, count #returning x1 and counter after the previous changes
            elif flag == "b": #if the user choose to do absolute relative approximate error, continue
                err = abs(x0-x1)/abs(x1) #setting the error to the value we get from |x0-x1|over|x1|
                if err < tolerance: #if the error is less than the user's tolerance, continue
                    return root, count #returning x1 and counter after the previous statements
            elif flag == "c": #if the user choose to do the estimated true absolute error, continue
                err = abs(original_function(x1)) #setting the error equal to the value we get from |function(x3)|
                if err < tolerance: #if the error is less than the user's tolerance, continue
                    return root, count #returning x2 and counter after the previous lines of code
            elif flag == "d": #if the user choose to do both absolute approximate & estimated true absolute error,continue
                err1 = abs(x0-x1) #set err1 equal to |(x3-x4)|
                err2 = abs(original_function(x0)) #set err2 equal to |function(x3)|
                if err1 < tolerance and err2 < tolerance: #if both errors are less than the user's tolerance, continue
                    return root, count #returning x2 and counter after previous actions
        x0 = x1 #setting x0 equal to x1