#6/13/20
"""
Problem Statement:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def longestCollatzSequence(n):
    longestColSequence = []
    for i in range(1,n+1,1):
        ColSequence = []
        while i != 1: #Stop once sequence reaches 1.
            ColSequence.append(i)
            if i % 2 == 0: #If even, divide current term by 2 to get next term.
                i = i // 2
            else: #If odd, multiply current term by 3 and add 1 to get next term.
                i = 3*i + 1
        ColSequence.append(i)
        if len(ColSequence) > len(longestColSequence):
            longestColSequence = ColSequence
    return longestColSequence, n

longestColSequence, n = longestCollatzSequence(999999)
print('The starting term under ' + "{:,}".format(n+1) + ' which produces the longest chain is')
print("{:,}".format(longestColSequence[0]) + ', which contains ' + str(len(longestColSequence)) + ' terms.')
#Answer = 837,799 with 525 terms

