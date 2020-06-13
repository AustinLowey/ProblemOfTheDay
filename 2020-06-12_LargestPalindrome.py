#6/12/20
"""
Problem Statement:
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def largestPalindrome(n):
    maxProduct, factor1, factor2 = 1, 1, 1
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            strFirstHalf, strSecHalf = str(i*j)[:len(str(i*j))//2], str(i*j)[len(str(i*j))//2:] #Split into 2 str's
            strSecHalf = strSecHalf[::-1] #Reverses second string
            if i*j > maxProduct and strFirstHalf == strSecHalf:
                factor1, factor2, maxProduct = i, j, i*j
    return factor1, factor2, maxProduct, n
        
f1, f2, maxProduct, n = largestPalindrome(999)
print('The largest palindrome made from the product of numbers up to ' + str(n))
print('is ' + str(maxProduct) + ' with factors of ' + str(f1) + ' and ' + str(f2) + '.')
#Answer is 906609 = 913 * 993