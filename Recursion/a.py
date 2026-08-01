def show(n):
    if (n==1):
        return 1
    else:
        print(n)
        show(n-1)
print(show(5))        

    