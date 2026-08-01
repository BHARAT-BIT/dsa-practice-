def remove_duplicates(arr):
    if not arr:
        return 0 
    slow = 0 
    for fast in range (1,len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1 
            arr[slow] = arr[fast]
    return slow+1
    
print(remove_duplicates(arr=[0]))
print(remove_duplicates(arr=[0,1,4,2,34,43,2,34,54,32,1,]))   