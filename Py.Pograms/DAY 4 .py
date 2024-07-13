#Find Missing No. in Array 

#first method is SUMMATION METHOD
def get_miss_summation (a):
    n=a[-1]
    total =n*(n+1)//2
    sum1 =sum(a)
    num =total-sum1
    print(num)



#second method is XOR METHOD
def get_miss_XOR (a):
    n =len(a)
    xor_a = a[0]
    for index in range (1,n):
        xor_a = xor_a^a[index]
    x2=0
    for index in range(1,n+2):
        x2=x2^index
    print(xor_a^x2)

a=[1,2,3,4,6,7,8]
get_miss_XOR (a)




