#06/07/2020
"""
Problem Statement:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

"""
First iteration below. This function finds all factors of n and then checks if each factor is prime.
The issue with this function is that it's very inefficient since the for loops evaluate all odd integers 
from 3 to n. Thus this function only works up to n's of around 10 million or so (for my pc spec's).
"""
def primeFactors1(n):
    primeFactors = []
    if n % 2 == 0: #add 2 as a prime factor if even number (since for loop only checks odd numbers)
        primeFactors.append(2)
    for i in range(3,n+1,2): #only checks odd numbers since even numbers (excluding 2) aren't prime
        if n % i == 0: #find all factors
            factors = []
            for j in range(3,i,2): #check if each factor is prime
                if i % j == 0:
                    factors.append(j)
            if len(factors) == 0: #if prime, append to list
                primeFactors.append(i)
    return primeFactors


"""
Second iteration below. Works by decomposing the number or in other words, checks to see if n is divisble
by i (which is the value 2 followed by a while-loop iterator for increasing odd integers starting at 3 (since
even numbers, excluding 2, aren't prime, thus speeding up the algorithm)) and if it is, divides n by i
to get an "updated" n. Checks to see if "updated" n is equal to 1, which indicates number has been
fully decomposed. Also has second while loop to check for multiple of the same prime factor, for
example 24 decomposes to 2*2*2*3, which has three 2's. This method ensures all returned i values are
prime and allows the while-loop odd-number iteration to stop at the highest prime number.
"""
def primeFactors2(n, returnRepeats=False):
    primeFactors = []
    while n % 2 ==0: #Having this while loop for i == 2 lets us change to "i=3" and "i=i+2" in the next while
                     #loop, which skips even numbers for i, making this function twice as fast for large numbers
        n = n // 2
        if returnRepeats == False:
            if 2 not in primeFactors: #This if statement prevents returning any repeats of prime factors
                primeFactors.append(2)
        elif returnRepeats == True:
            primeFactors.append(2)
    i = 3
    if returnRepeats == False: #No prime factor repeats are returned. ex: [2*2*2*3] --> [2,3]
        while n != 1:
            while n % i == 0: #Using while instead of if here checks for repeats of i in decomposition (i.e. 24=2*2*2*3)
                n = n // i #Decompose
                if i not in primeFactors: #This if statement prevents returning any repeats of prime factors
                    primeFactors.append(i)
            i = i + 2
    elif returnRepeats == True: #All prime factor repeats are returned. ex: [2*2*2*3] --> [2,2,2,3]
        while n != 1:
            while n % i == 0: #Using while instead of if here checks for repeats of i in decomposition (i.e. 24=2*2*2*3)
                n = n // i #Decompose
                primeFactors.append(i)
            i = i + 2
    return primeFactors


"""
Third iteration below. The same as iteration 2 except instead of using a while-loop + counter as an 
iterator for i, I simply imported a list of prime numbers to use for i. This is significantly less 
computationally intensive, but it felt a little like cheating for this problem so I saved it for last.
"""
def primeFactors3(n, returnRepeats=False):
    primeFactors = []
    with open('2020-06-07_Primes1to1000k.txt', 'r') as reader: #Open text file. Prime numbers b/w 1-1mil from mathisfun.com
        allPrimeNumbers = list(map(int, reader.read().splitlines())) #import numbers
    if returnRepeats == False:
        while n != 1:
            for i in allPrimeNumbers: #Major change from iteration #2 is change from counter (i=i+2) to this for-loop.
                while n % i == 0:
                    n = n // i
                    if i not in primeFactors:
                        primeFactors.append(i)
    elif returnRepeats == True:
        while n != 1:
            for i in allPrimeNumbers: #Major change from iteration #2 is change from counter (i=i+2) to this for-loop.
                while n % i == 0:
                    n = n // i
                    primeFactors.append(i)
    return primeFactors
    