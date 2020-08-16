#8/15/20
"""
Problem Statement:
Using a function rand7() that returns an integer from 1 to 7 (inclusive) 
with uniform probability, implement a function rand5() that returns an 
integer from 1 to 5 (inclusive).
"""

"""
Note: Problem statement doesn't require that the integer returned from rand5() 
has uniform probability for integers 1-5, so rand5() could technically just 
return a fixed integer. That being said, I implemented rand5() to return
with uniform probability.
"""

import random

def rand7():
    return random.randint(1,7) #Return random integer between 1 and 7.

def rand5():
    n = 8
    while n > 5: #71.4% (5/7) probability that a number 1-5 is picked, each with
                 #uniform probability. 28.6% (2/7) probability that rand7() will
                 #simply be called again if rand7() returns 6 or 7.
        n = rand7()
    return n

x = rand5()
print(x)