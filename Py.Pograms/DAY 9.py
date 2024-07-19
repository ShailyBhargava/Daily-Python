def min_diff(a):
    a = sorted(a)
    size = len(a)
    min_diff = -9999*999

    for i in range(size-1):
        if(a[i+1] - a[i] > min_diff):
             min_diff = a[i+1] - a[i]

    return min_diff


a= [8,4,31,12,45,67,48,69,5]

print("Mininmum difference Between elements of an array is " ,min_diff(a))