

def reverse_word(str):
    n =len(str)
    if(n==1):
        return str
    str2 = str.split(" ")
    rev_all=""
    for i in range(len(str2)):
        rev= reverse(str2[i])
        rev_all = rev_all + rev+ " "
    print(reverse(rev_all) )
str ="python is object oriented and highly efficient programming language"
print(reverse_word(str))