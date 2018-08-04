#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 18:22:48 2018

@author: lakshmi
"""

#Write an iterative function iterPower(base, exp) that calculates the exponential by simply using successive multiplication.
# For example, iterPower(base, exp) should compute by multiplying base times itself exp times.
# Write such a function below.
# This function should take in two values - base can be a float or an integer; exp will be an integer.
# It should return one numerical value.
# Your code must be iterative 
# Use of the ** operator is not allowed. 

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result

print(iterPower(0, 0))


