def freq_word():
    input_str = input("Enter the string: ")
    
   
    words_list = input_str.split()
    
    # Create a dictionary to store word frequencies
    freq_dict = {}
   
    for word in words_list: # Count the frequency of each word
        if word not in freq_dict:
            freq_dict[word] = 0
        freq_dict[word] += 1
    
    
    print(freq_dict)

freq_word() #function calling

