arr = [5, 15, 25, 35, 45, 55]
left = 0 
right = len(arr)-1 
while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1

print (arr)    