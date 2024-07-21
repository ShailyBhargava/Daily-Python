#remove duplicate from array 
#method 1 by creating another array sapce complexity is O(n)

def rem_duplicate(a):
    n=len(a)
    if(n==0 or n==1):
        return a
    temp = [0]*n
    pivot =0
    for last in range(0,n-1):
     if a[last] != a[last+1]:
        temp[pivot] = a[last]
        pivot=pivot+1
    temp[pivot] = a[n-1]
    return temp [0:pivot+1]

a= [1,2,2,2,3,3,4,4,4,4,4,5,5,5,5,6,6]

print(rem_duplicate(a))
