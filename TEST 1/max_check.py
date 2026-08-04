def find_max(lst):
    max=0
    for i in lst:
        if i > max:
            max = i
        return max
lst=[2,3,4,5,6,7,8,9,10]
print(f"The maximum number in the list is: {find_max(lst)}")        