#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Sri Rupin Potula
from sys import maxsize # import max int for initialization

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9] # initialize the input array
ans = -maxsize - 1 # initialize ans variable to -intmax

# WRITE YOUR CODE HERE
def help(arr, low, high, mid):
    l_max=maxsize-1
    r_max=-maxsize-1
    for i in range(low, mid+1):
        l_max=min(l_max,arr[i])
    for i in range(mid+1, high+1):
        r_max=max(r_max,arr[i])
    return r_max-l_max

    
def divide_and_conquer(arr, low, high):
    if low>=high:
        return 0
    mid = (low+high)//2
    left_half = divide_and_conquer(arr,low, mid)
    right_half = divide_and_conquer(arr, mid+1, high)
    total_min = help(arr, low, high, mid)
    return max(left_half, right_half,total_min)


low =0
high = len(arr)-1
ans = divide_and_conquer(arr, low, high)

print(ans) # printing the answer
