#find out the sum of those pairs which are equal to the target value

def twosum(a,target):
    a.sort()
    left =0
    right = len(a)-1
    while(left<=right):
        if(a[left]+a[right]<target):
         left += 1
        elif(a[left]+a[right]>target):
           right -= 1
        elif(a[left]+a[right] == target):
           print ("Values of pair are:",a[left],"&",a[right])
           right =right-1
           left = left+1

a= [2,4,7,1,6,5,11,8,9,13]
target =15
twosum(a ,target)
