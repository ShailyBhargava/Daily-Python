list1 = []
list = [5,8,0,7,2,7]
#print(list1)
#list2= reversed(list)
#my_string = " ".join(map(str, list1))
#print(my_string)

#reverse the list without using any builtin function

for i in range(len(list)-1,-1,-1):
    list1.append(list[i])
print(list1)