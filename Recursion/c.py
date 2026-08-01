def sum_of_numbers(n):
    if n ==0 :
        return 0
    return n + sum_of_numbers(n-1)
n=int(input("Enter a number: "))
print(f"The sum of numbers from 1 to {n} is {sum_of_numbers(n)}")  
    