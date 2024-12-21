
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Sri Rupin Potula
from sys import maxsize
arr = [15, 13, 8, 14, 12, 9, 10, 15, 9] # initialize the input array
ans = 0
# WRITE YOUR CODE HERE
minimum_profit=arr[0]
size = len(arr)
for i in range(1, size):
    profit = arr[i]-minimum_profit
    ans = max(profit, ans)
    minimum_profit = min(arr[i], minimum_profit)

print(ans) # printing the max possible subarray sum, as ans
