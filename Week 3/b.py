# def palindrome_check(s):
#     left = 0 
#     right = len(s)-1
#     while left < right :
#         if s[left] == s[right]:
#             left += 1
#             right -= 1 
#         else:
#             return False    
#     return True 

# result = palindrome_check("racecar")
# print(result)




# def palindrome_check(s):
#     cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    
#     left = 0
#     right = len(cleaned) - 1
#     while left < right:
#         if cleaned[left] == cleaned[right]:
#             left += 1
#             right -= 1
#         else:
#             return False
#     return True










def palindrome_check(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # skip non-alphanumeric from the left
        while left < right and not s[left].isalnum():
            left += 1
        # skip non-alphanumeric from the right
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
result1 = palindrome_check("A man, a plan, a canal: Panama")
result2 = palindrome_check("race a car")
print(result1)
print(result2)