arr = [1, 3, 5, 7, 9 , 11, 12, 7, 6, 87, 5, 4, 0, 99, 6]
k = 2 
window_sum = sum(arr[:k])
max_sum = 0

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum , window_sum)

print(max_sum)    