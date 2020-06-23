#6/22/20
"""
Problem Statement:
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d_n represents the nth digit of the fractional part, find the value of the following expression.

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""

champ, n, i = '.'
n = len(champ)
i = 1
while n < 1000001: #Generate Champernownes Constant to 1 million digits
    champ = champ + str(i)
    n = len(champ)
    i += 1

#Solve:
solution = (int(champ[1]) * int(champ[10]) * int(champ[100]) * int(champ[1000]) * 
            int(champ[10000]) * int(champ[100000]) * int(champ[1000000]))