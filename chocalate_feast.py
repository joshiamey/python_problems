#!/bin/python3

import sys

def calculate_candies(n,c,m):
    candies = int(n/c)    
    available = candies
    
    while available >= m :
        xchanged = int(available/m)
        available = int(available % m)
        available += int((xchanged+available)/m)
        print(available)
        candies += xchanged  


    print(candies)


calculate_candies(6,2,2)
# t = int(input().strip())
# for a0 in range(t):
#     n,c,m = input().strip().split(' ')
#     n,c,m = [int(n),int(c),int(m)]
#     calculate_candies(n,c,m)
    

