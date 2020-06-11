#6/10/20
"""
Problem Statement:
Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def listReturnSum(k,L):
    numsAddToK = False
    solutions = []
    for i in L:
        for j in L:
            if i+j == k:
                numsAddToK = True
                solutions.append((i,j)) #Not required by problem statement, but I did it anyway.
    for i in solutions: #Removes duplicate solutions
        for j,m in enumerate(solutions):
            if i[0] == m[1]:
                solutions.pop(j)
    return numsAddToK, solutions

#This is a very 'brute force' solution, though it does work. Will look to 
#revisit this problem in the future for a cleaner solution. Also worth noting
#that I made the assumption that numbers in L can be repeated.

#Verificaton:
k = 17   
L = [10,15,3,7] 
numsAddToK, solutions = listReturnSum(k,L) #True: (10, 7)

#Using function on other lists and k's:
k2, L2 = 86, [12, 23, 60, 25, 18, 13, 11]
numsAddToK2, solutions2 = listReturnSum(k2, L2) #False: No solutions
k3, L3 = 86, [12, 23, 60, 26, 18, 13, 63]
numsAddToK3, solutions3 = listReturnSum(k3, L3) #True: (23, 63) and (60, 26)