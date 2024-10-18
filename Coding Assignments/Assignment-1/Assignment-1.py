#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@author: Sri Rupin Potula


''' --- Input values --- '''
M = [ [2, 1, 4, 5, 3],              # Department preference list
     [4, 2, 1, 3, 5], 
     [2, 5, 3, 4, 1], 
     [1, 4, 3, 2, 5], 
     [2, 4, 1, 5, 3] ]
W = [ [5, 1, 2, 4, 3],              # Employee preference list
     [3, 2, 4, 1, 5], 
     [2, 3, 4, 5, 1], 
     [1, 5, 4, 3, 2], 
     [4, 2, 5, 3, 1] ]
N = 5                               # Number of department & employee



# WRITE YOUR CODE HERE
#import queue 
from queue import Queue
q= Queue(maxsize=N)

for i in range(1,6):
    q.put(i)

#list of mappings
women_occupied = []
for i in range(N):
    women_occupied.append(-1)
    

    
men_occupied = []
for i in range(N):
    men_occupied.append(-1)
#print("Men Occupied: ", men_occupied)
    
#Inverse Matrix Caculation for Women
for i in range(N):
    women_list=W[i]
    inverse_list=[-1,-1,-1,-1,-1]
    for j in range(N):
        element=women_list[j]
        inverse_list[element-1]=j
    W[i]=inverse_list

#Gale-Shapeley Algorithm
while q.empty()!=True:
    man_to_get_engaged = q.get()
    man_pref = M[man_to_get_engaged-1]
    for i in man_pref:
        choice_man = i-1
        if (women_occupied[choice_man]==-1):
            women_occupied[choice_man]=man_to_get_engaged
            men_occupied[man_to_get_engaged-1]=i
            break
        else:
            current_choice = women_occupied[choice_man]
            if (W[choice_man][man_to_get_engaged - 1] < W[choice_man][current_choice -1]):
                women_occupied[choice_man]=man_to_get_engaged
                men_occupied[man_to_get_engaged-1]=i
                q.put(current_choice)
                break

employee=[]
employee=women_occupied

''' --- Visualizing the result, Printing the output --- '''
Names = [ ['HR', 'CRM', 'Admin', 'Research', 'Development'],      # Initialize the mapping of names
         ['Adam', 'Bob', 'Clare', 'Diane', 'Emily'] ]
print('Result is:-')
for i in range(N):
    print(Names[0][i], ":", Names[1][employee[i]-1])                # Map the result to the names


