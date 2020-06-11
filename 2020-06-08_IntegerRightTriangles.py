#06/08/2020
"""
Problem Statement:
If p is the perimeter of a right angle triangle with integral length sides, 
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

"""
Work/thought before start coding:
    
a^2 + b^2 = c^2 -->
p = a + b + c   --> c = p - a - b
p and a will be iterated and thus a and b are 2 unknowns. We have 2 equations
and 2 unknowns so we can solve.
Substitute c from perimeter equation into the first Pythagorean theorem equation:
a^2 + b^2 = (p-a-b)^2 = p^2 + a^2 + b^2 - 2pa - 2pb + 2ab
2pb - 2ab = p^2 - 2pa
b = (p^2 - 2pa) / (2p - 2a)

Calculate b for all integers a. If b % 1 == 0: b is an integer (one of multiple ways to check this)

Iterate all p values from 1 to 1,000, create list of solutions, and measure length
of this list. Compare current list length to previous max list length and if current
one is longer, update max list length with current.
"""

import math #to use square root function

def intRightTri(p):
    solutionsForMax = []
    for p in range(1, p+1, 1): #Iterates for all values of p from 1 to 1000 (or whatever p user inputs).
        abc = []
        for a in range(1, p, 1): #Iterates for all a integers from 1 to current p value.
            b = (p*p - 2*p*a) / (2*p - 2*a) #Calculate corresponding b using earlier equation for each a integer.
            if (b % 1 == 0) and (a != 0) and (b !=0) and (a>0) and (b>0): #Solution found when b is integer and a,b are both real numbers.
                c = math.sqrt(a*a + b*b) #Calculate c for each solution.
                b, c = int(b), int(c)
                abc.append((a,b,c)) #Append tuple to list of solutions for CURRENT p.
                if len(abc) > len(solutionsForMax): #If current p has more solutions than previous max p:
                    solutionsForMax = abc #Update solutions for previous p with those of current p.
                    pMax = p #Update previous p with current p.
    del solutionsForMax[len(solutionsForMax)//2:len(solutionsForMax)]
    """Above line is since we haven't yet addressed repeats of the same solution when 'c' is the same as a previous 'c' and 'a'
    is the same as a previous 'b' and vice versa. In retrospect, a better way to address this would be to iterate and test p-values
    for up to half of the user-entered p instead, as this would shorten the execution time, which would be valuable for higher 
    user-entered p's.
    """
    return solutionsForMax, pMax, p

solutionsForMax, pMax, p = intRightTri(1000) #Solve problem. If solving for p ≤ another number, enter that number here.

print('For values of p ≤ 1000, the number of solutions is maximized at ' + 
      str(len(solutionsForMax)) + ' solutions when p = ' + str(pMax) + '.\n')
print('The solutions are:')
print(solutionsForMax)