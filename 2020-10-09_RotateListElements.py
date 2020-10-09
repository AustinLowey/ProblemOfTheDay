#10/9/20
"""Problem Statement:
Write a function that rotates a list by k elements. For example, 
[1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 
Try solving this without creating a copy of the list. How many 
swap or move operations do you need?"""

def rotate_elements(L, k):
    L = L + L[:k] #Modify list in place to add k # of elements to end of list.
    del L[:k] #Delete k # of elements from beginning of list.
    return L

L = [1, 2, 3, 4, 5, 6]
k = 2
ans = rotate_elements(L,k)
print(ans) #Prints [3, 4, 5, 6, 1, 2]