def summ(str):
    if str=="":
        return 
    return int(str[0]) + summ(str[1:])
n=int(input("Enter a number: "))
print(f"The sum of digits of {n} is {summ(str(n))}")