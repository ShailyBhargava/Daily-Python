def list_to_dict():
    keys =[1,2,3,4]
    values =["A","B","C","D"]
    result=dict(zip(keys,values))
    print(result)

def dict_to_list():
    d={1: 'A', 2: 'B', 3: 'C', 4: 'D'}
    for i in d.items():
        print(i)
dict_to_list()
list_to_dict()
