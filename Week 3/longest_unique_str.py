def longest_unique_str(s):
    seen = {}
    left = 0 
    max_length = 0 

    for right , ch  in enumerate(s):
        if ch in seen and seen[ch] >=left:
            left = seen[ch]+1
        else:
            seen[ch]= right     
        max_length = max(max_length , right - left+ 1)
    return max_length
result = longest_unique_str("abcabcbb")
print(result)