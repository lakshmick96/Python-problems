#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:37:22 2018

@author: lakshmi
"""

#Write a function recurPower(base, exp) which computes (base^exp) by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.
#This function should take in two values - base can be a float or an integer; exp will be an integer
# It should return one numerical value. 
#Your code must be recursive.
#Use of the ** operator or looping constructs is not allowed. 

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)    
print(recurPower(0, 0))