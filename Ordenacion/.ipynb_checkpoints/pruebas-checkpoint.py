# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:46:03 2018

@author: Merlin The Sorcerer
"""

import random as rand
import numpy as np
import timeit
import ordenaciones

x1 = []
x2 = []
x3 = []

for i in range(100000):
    x1.append(rand.random())
    

def insertionSortTest():
    insertionSort(x1)

def bubbleSortTest():
    bubbleSort(x1)
    
print('Insertion : ' + str(timeit.timeit(insertionSortTest, number = 1)))
print('Bubble    : ' + str(timeit.timeit(bubbleSortTest, number = 1)))

