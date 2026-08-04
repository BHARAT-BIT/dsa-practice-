def rev_str(s):
    if s=="":
        return""
    return s[-1]+rev_str(s[:-1])
s=input("Enter a string: ")
print(f"The reverse of {s} is {rev_str(s)}")
    