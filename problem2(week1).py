#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:20:33 2018

@author: lakshmi
"""

#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print:
#Number of times bob occurs is: 2


s = input("Enter the string : ")
n = 0
for i in range(len(s)):
    if s[i:].startswith('bob'):
        n += 1
print('Number of times bob occurs is: ' , str(n))

