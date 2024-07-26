def first_non_repeat(s):
    dict = {}
    size = len(s)
    

    for i in range(size):
        key = s[i]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] += 1

    
    count = 0
    for index in range(size):
        if dict[s[index]] == 1:
            return s[index], count
        count += 1
    
    # If no non-repeating character is found
    return None, -1

s = "btsbtsbts"
print(first_non_repeat(s))
