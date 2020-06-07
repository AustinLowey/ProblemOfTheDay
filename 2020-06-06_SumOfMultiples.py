#06/06/2020
"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

#First test with 10:
def sumOfMultiples(n):
    x = sum([i for i in range(1,n,1) if i % 3 == 0 or i % 5 == 0])
    print(x)
    return x

#Verification:
n10 = sumOfMultiples(10)
n22 = sumOfMultiples(22)

#Answer to the problem statement:
n1000 = sumOfMultiples(1000)


"""
Expanding on this problem statement, I added the functionality to choose
which multiples to use (instead of just 3 and 5).
"""

def sumOfChosenMultiples(n, x1, x2):
    x = sum([i for i in range(1,n,1) if i % x1 == 0 or i % x2 == 0])
    print(x)
    return x

#Verification:
y1 = sumOfChosenMultiples(1000, 3, 5)

#For n=5000, and multiples = 10,12
y2 = sumOfChosenMultiples(5000, 10, 12)