# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:46:06 2024

@author: User
"""
#HOME WORK 2
# Textbook Reading: finish the first three chapters
# Import cmath as m …. Use m.sqrt(X); use inputs and float()
# A. The standard form of a quadratic equation is:
# ax2 + bx + c = 0, where a, b and c are real numbers and a ≠ 0  Write a program to solve this equation. The program should take a,b,c as input from user. (You may need to import math or cmath module.)
# B. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. If the number is a multiple of 4, print out a different message.
# C. Class project Proposal due in 2 weeks 
# What to turn in : 
# Code and output
# Code comment section explains program and also your name & date etc

import cmath as m

def quadratic_equation ():
    #convert from strings to numbers : int() or float()
    a = float(input('please input a real number "a" (a # 0): '))
    b = float(input('please input a real number "b": '))
    c = float(input('please input a real number "c": '))
    print(f'The equation is: {a}x^2 + {b}x + {c} = 0')
    
    E= b**2-4*a*c
    print (f'discriminant = {E}')
    # ax2 + bx + c = 0
    # x= (-b+/- sqrt(b^2-4ac))/2a
    if a!=0:
        if E == 0:
            print ('there is one value of x')
            x = (-b+m.sqrt(E))/(2*a)
            print(f'x = {x}')
        elif E > 0:
            print ('there are two values of x')
            x1 = (-b + m.sqrt(E)) / (2*a)
            x2 = (-b - m.sqrt(E)) / (2*a)
            print(f'x1 = {x1}')
            print(f'x2 = {x2}')
        else: E < 0
        print('There are two complex values of x.')
        x1 = (-b + m.sqrt(E)) / (2*a)
        x2 = (-b - m.sqrt(E)) / (2*a)
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
    else: print('please input a real number "a" with "a" # 0')
quadratic_equation ()   

def even_odd():
    number = int(input('Please input a number: '))
    if number % 4 == 0:
        print(f'{number} is a multiple of 4')
    elif number % 2 == 0:
        print(f'{number} is even')
    else: 
        print(f'{number} is odd')
even_odd()

































