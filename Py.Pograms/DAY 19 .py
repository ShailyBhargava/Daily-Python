def romaninteger(s):
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    i = 0
    while i < len(s):
        curr = roman_to_int[s[i]]
        if i + 1 < len(s):
            next = roman_to_int[s[i + 1]]
        else:
            next = 0
        
        if curr >= next:
            total += curr
            i += 1
        else:
            total += next - curr
            i += 2
            
    return total

print(romaninteger("CXLLIVI"))
