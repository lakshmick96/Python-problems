#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:15:23 2018

@author: lakshmi
"""

#To find the most common words of a song lyrics

lyrics = ['ba', 'ba', 'black', 'sheep', 'have', 'you', 'any', 'wool', 'yes', 'sir', 'yes', 'sir',]
def most_common_words(lyrics):
    my_dict = {}
    for word in lyrics:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    values = my_dict.values()
    best = max(values)
    words = []
    for k in my_dict:
        if my_dict[k] == best:
            words.append(k)
    return words

print(most_common_words(lyrics))
