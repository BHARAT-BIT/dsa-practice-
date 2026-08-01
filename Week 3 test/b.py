def subarray(nums,k):
    count = 0
    prefix_sum = 0 
    seen = {0:1}

    for i in nums:
        prefix_sum += i 
        revised_sum = prefix_sum - k 

        if revised_sum in seen:
            count += seen[revised_sum]

        if prefix_sum in seen:
            seen[prefix_sum] += 1 

        else:
            seen[prefix_sum] = 1

    return count 



nums = [1, 1, 1]
k = 2

print(subarray(nums,k))