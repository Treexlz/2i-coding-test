# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:30:28 2022

@author: scott
"""

def print_multiples(A, X, Print=False):
    # function takes multiple A and iterates it to find all values 
    # within a given limit X
    
    # create empty lists to hold A to X, A+1 to 2X and A+2 to 3X 
    x_1 = []
    x_2 = []
    x_3 = []
    
    # X // A to calculate how many multiples within given range
    # then iterate through each possible multiple and times by A
    # then add to a list
    for i in range(1, X // (A+1)):
        x_1.append(i * A)

    for j in range(1, (2*X) // (A+2)):
        x_2.append(j * (A+1))

    for k in range(1, (3*X) // (A+3)):
        x_3.append(k * (A+2))

    # allow priting of lists by setting calling True in function
    if Print == True:
        print("A to X:", x_1)
        print("A+1 to 2X:", x_2)
        print("A+2 to 3X", x_3)
        
print_multiples(3, 100, True)