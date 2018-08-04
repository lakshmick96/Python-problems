#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:07:55 2018

@author: lakshmi
"""

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5

s = input("Enter the string: ")
num = 0
for char in s:
      if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        num += 1
print("Number of vowels: " + str(num))
