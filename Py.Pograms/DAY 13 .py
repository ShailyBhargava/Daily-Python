def max_sum(a):
    size = len(a)
    sum = 0
    max_sum = a[0]
    for i in range(size):
        sum = sum + a[i]
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum

a = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]
print(max_sum(a))
