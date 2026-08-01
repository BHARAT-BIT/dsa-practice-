def two_sum_optimized(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i ]

        seen[nums[i]] = i 
    return []
            
nums = [2, 7 , 6, 6, 4]
target = 9

print(two_sum_optimized(nums , target))




































# def two_sum(nums, target):
#     seen = {}

#     for i in range(len(nums)):
#         complement = target - nums[i]

#         if complement in seen:
#             return [seen[complement], i]

#         seen[nums[i]] = i

# nums = [2, 7, 11, 15]
# target = 9

# print(two_sum(nums, target))