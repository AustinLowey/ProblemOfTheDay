#6/9/20
"""
Problem Statement:
Given an array of integers, find the first missing positive integer in 
linear time and constant space. In other words, find the lowest positive 
integer that does not exist in the array. The array can contain duplicates 
and negative numbers as well. You can modify the input array in-place.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.
"""

def lowestIntNotInArray(L):
    i = 1
    while i in L:
        i += 1
    return i
        
#Verification:
x = lowestIntNotInArray([3,4,-1,1])
x2 = lowestIntNotInArray([1,2,0])
print(x, x2)
