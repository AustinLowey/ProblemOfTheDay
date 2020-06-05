#06/05/2020
"""
Problem Statement:
There's a staircase with n steps, and you can climb 1 or 2 steps at a time. Given n, write a function
that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if n is 4, then there are 5 unique ways:
[1,1,1,1] , [2,1,1] , [1,2,1] , [1,1,2] , [2,2]
"""

"""
Work/Thought before starting to write program:
    
Let y = number of unique ways

For n=1: y=1 [1]
For n=2: y=2 [1,1] and [2]
For n=3: y=3 [1,1,1] , [1,2] , [2,1]
For n=4: y=5 [1,1,1,1] , [1,1,2] , [1,2,1] , [2,1,1] , [2,2]
For n=5: y=8 [1,1,1,1,1] , [1,1,1,2] , [1,1,2,1] , [1,2,1,1] , [2,1,1,1] , [1,2,2] , [2,1,2] , [2,2,1]
For n=6: y=13 [1,1,1,1,1,1] , [2,1,1,1,1] , [1,2,1,1,1] , [1,1,2,1,1] , [1,1,1,2,1] , [1,1,1,1,2] , 
              [2,2,1,1] , [2,1,2,1] , [2,1,1,2] , [1,2,2,1] , [1,2,1,2] , [1,1,2,2] , [2,2,2]

Pattern identified --> y_n = y_(n-1) + y_(n-2) --> i.e. Fibonacci sequence
                   --> Ex: For n=6, y_6 = y_5 + y_4 = 8 + 5 = 13

For verifying higher numbers, it will be useful to use combinations equation, i.e. nCr or C(n,r)                  
For n=7: y=21 -->   For all 1's: [1,1,1,1,1,1,1] (x1)
                    For 1 2:     [2,1,1,1,1,1] (x6) since 6 locations for the 2 --> nCr = 6C1 = 6
                    For 2 2's:   [2,2,1,1,1,] (x10) since 5 locations for 2 2's --> nCr = 5C2 = 10
                    For 3 2's:   [2,2,2,1] (x4) since 4 locations for the 1     --> nCr = 4C1 = 4
                    Therefore, y = 1 + 6C1 + 5C2 + 4C1 = 21
"""

def stairCalculator(n):
    #nTermsList = [y for i in...] add list comprehension later?
    nTermsList = [0, 1, 2] #for n=0,1,2
    for i in range(3,n+1,1):
        y = nTermsList[-1] + nTermsList[-2]
        nTermsList.append(y)
    return nTermsList, n

allTerms, n = stairCalculator(7) #change input n here

print('For n = ' + str(n) + ':')
print('There are ' + str(allTerms[n]) + ' unique ways to climb the staircase.')
if n>1: #since I initialized nTermsList for n=1 and n=2
    print('\nThe number of unique ways for n-values of 0 through ' + str(n) + ' are:\n' + str(allTerms))

