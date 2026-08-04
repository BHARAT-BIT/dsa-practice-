arr = [2, 1, 5, 2, 3, 2]
target = 7
best_score = len(arr) 
current_sum = 0
left = 0 
for right in range(0,len(arr)):
    current_sum += arr[right]
    
    while current_sum >= target:
        current_score = right - left +1 
        current_sum -= arr[left]
        
        left +=1
        best_score = min(current_score , best_score)  
    

print(best_score)