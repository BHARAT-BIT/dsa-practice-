def fact(n):
    if n==0 or n==1:
        return 1
    else:
        factorial= n *fact(n-1)
    return factorial
n=int(input("Enter a number: "))
print(f"The factorial of {n} is {fact(n)}")