# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Brandon Azevedo
#
# Date: 1/31/21
# 
##################################################
#
# Sample Script for Assignment 2: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

import math
math.pi

import math
math.e
"""For Logit link function
"""

##################################################
# Function Definitions
##################################################


#####
#Example 1
#####


def average(num1,num2):
    """Return the average of num1 + num2
    """
    
    return( (num1 + num2) / 2)

print(average(3,7))

print(average(8,10))

print(average(20,50))

#Got 5, 9, 35 All correct


#####
#Example 2
#####


def area_of_circle(Radius):
    
    return ((math.pi)*Radius**2)
    
print(area_of_circle(5))

print(area_of_circle(8))

print(area_of_circle(15))

#Got 78.539, 201.061, 706.857 All correct

#####
#Example 3
#####

def Volume_of_cylinder(Radius,Height):
    
    return (Height*(math.pi)*Radius**2)

print (Volume_of_cylinder(5,10))

print (Volume_of_cylinder(10,15))

print (Volume_of_cylinder(20,50))


#Got 785.3975, 4712.385, 62831.8 All correct

#####
#Example 4
#####

def Utility(x,y,a):
    
    """This is the Cobb Douglas utiluty function
    """
    
    return((x**a) * ((y)**(1 -a)))

print(Utility(1,2,5))

print(Utility(1,3,8))

print(Utility(5,8,9))

#Got answers of   0.0625, 0.0004572473708276177, 0.11641532182693481 


###
#Example 5
###

def logit(x,B0,B1):
    """This will calculate the logit link function with arguments of x, B0, and B1
    """
  
    return((math.e **(B0+(x*B1)))/(1+(math.e**(B0+(x*B1)))))



#QUESTION 2 (Honestly I had no idea how to do this part and don't have enough time to finish it, I think my prints above kinda answer it)