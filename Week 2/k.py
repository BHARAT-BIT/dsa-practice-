arr = [4, 2, 1, 7, 8, 3]
k = 2 
window_sum = sum(arr[:k])
max_sum = window_sum 
 
for i in range(k,len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum,window_sum)

print(max_sum)    