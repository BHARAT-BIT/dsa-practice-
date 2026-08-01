def is_pal(s):
    if s == " " or len(s) == 0:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_pal(s[1:-1])

s=input("Enter a string: ")
is_palindrome = is_pal(s)