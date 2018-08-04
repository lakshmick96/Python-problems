#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 19:05:31 2018

@author: lakshmi
"""
#write a procedure which returns the key corresponding to entry with largest number of values associated with it.


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    
    length = []
    key = []
    for i in aDict.values():
        length.append(len(i))
    for i in aDict.keys():
        key.append(i)
    best = max(length)
    for i in range(len(length)):
        if length[i] == best:
            return key[i]
print(biggest(animals))
