# rotation of string

def rotate_str(s):
    temp = s+s
    for i in range (len(s)):
        for j in range(len(s)):
            print(temp[i+j],end =" ")
        print()

s = "PYTHON"
rotate_str(s)
