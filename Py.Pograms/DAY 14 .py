# find largest element in array
def largest(a):
    max = a[0]
    size = len(a)
    for i in range(size):
        if(max < a[i]):
            max =a[i]
    return max
a= [22,44,55,66,44,33,88,99,55,33]
print(largest(a))