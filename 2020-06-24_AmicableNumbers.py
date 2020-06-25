#6/24/20
"""
Problem Statement:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a 
and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

input = 10000

sumsOfDivisors = [(0,0)] #List of tuples. Each tuple is (n,d(n))
for n in range(1,input+1,1): #Find sum of divisors for each n and store in list d_n.
    divisors = []
    for i in range(1,n,1): #Find all divisors. Only go up to n instead of n+1 in order to exclude n from divisors.
        if n % i == 0:
            divisors.append(i)
    sumsOfDivisors.append((n, sum(divisors))) #(n,d(n))

#Check for amicable pairs:
amicableNumbers = []
for a, d_a in sumsOfDivisors:
    for b, d_b in sumsOfDivisors[a+1:]: #Using [a+1:] here improves runtime since checks for amicable pairs 
                                        #in only the remainder of the list. Eliminates redundancy.
        if d_b == a and d_a == b: #Checks amicable pair criteria
            amicableNumbers.append(a)
            amicableNumbers.append(d_a) #Need to append both a and d_a because used [a+1:] earlier.
            
print(sum(amicableNumbers)) #Prints solution, which is 31626