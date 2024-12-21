#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Sri Rupin Potula

from sys import maxsize                        # import max int for initialization

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]        # initialize the input array
ans = -maxsize - 1                             # initialize ans variable to -intmax

# WRITE YOUR CODE HERE

for i in range(0, len(arr)):
    sum=0
    for j in range(i+1, len(arr)):
        sum = arr[j]-arr[i]
        ans = max(ans, sum)

print(ans)                                # printing the answer