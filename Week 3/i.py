def first_unique_char(s):
    freq={}

    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch] = 1 

    for value in s:
        if freq[value] == 1:
            return s.index(value)
    return -1 

result = first_unique_char("leecode")
print(result)     

