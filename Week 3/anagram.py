# def is_anagram(s,t):
#     s = s.lower()
#     t = t.lower()
#     if len(s) != len (t):
#         return False
#     count = {}

#     for ch in s:
#         if ch in count:
#             count[ch] += 1
#         else:
#             count[ch] = 1 

 
#     for ch in t:
#         if ch in count:
#             count[ch] -= 1 
#         else:
#             return False 

#     for value in count.values():
#         if value != 0:
#             return False
#     return True 

             
# result = is_anagram("nagaRAm", "aNagRam") 
# print(result)
  



from collections import Counter

def is_anagram(s, t):
    return Counter(s.lower()) == Counter(t.lower())
result = is_anagram("nagaRAm", "aNagRam") 
print(result)
  