def ptrn_matc(s1,s2):
    if len(s1) != len(s2):
        return False 
    new_str = s1+s1 
    if s2 in new_str:
        return True 
    return False 

result = ptrn_matc("waterbottle", "erbottlewat")
print(result)