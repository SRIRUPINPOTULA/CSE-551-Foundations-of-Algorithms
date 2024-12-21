#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Sri Rupin Potula

w1 = "professor"
w2 = "confession"
ans = 0                                   # initialize ans variable to 0

# WRITE YOUR CODE HERE
def dp(i, j, memo):
    if i==0:
        return j
    if j==0:
        return i
    
    if (i,j) in memo:
        return memo[(i,j)]
    
    if w1[i-1]==w2[j-1]:
        memo[(i, j)] = dp(i - 1, j - 1, memo)
    else:
        insert = dp(i, j-1, memo)
        delete = dp(i-1, j, memo)
        replace = dp(i-1, j-1, memo)
        memo[(i, j)] = 1 + min(insert, delete, replace)
    
    return memo[(i,j)]
        
    
def main(w1, w2):
    memo = {}
    res = dp(len(w1), len(w2), memo)
    return res

ans = main(w1,w2)
    
print(ans)                                     # printing the answer