#anagrams

def anagrams(A):
    if(A==0):
        return
    else:
        dict={}
        for i in range(len(A)):
            word = ''.join(sorted(A[i]))
            if(word not in dict):
                dict[word] = [i+1]
            else:
                dict[word].append(i+1)


        return dict
    
A = ["cat","pot","top","dog","god","act","tca"]
print(anagrams(A))