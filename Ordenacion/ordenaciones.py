# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:44:10 2018

@author: Merlin The Sorcerer
"""



"Bubble sort"
def bubbleSort(a):
    "a = b.copy()"
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
    "return a"

"Insertion Sort"
def insertionSort(a):
    "a = b.copy()"
    for i in range(len(a)):
        minIndex = i
        for j in range(i+1, len(a)):
            if a[minIndex] > a[j]:
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]
    "return a"

def isSortedAsc(a):
    return all(a[i] <= a[i+1] for i in range(len(a) - 1))

def isSortedDesc(a):
    return all(a[i] >= a[i+1] for i in range(len(a) - 1))