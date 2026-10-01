import heapq

nums = [5, 3, 8, 1, 2, 9, 4]
heapq.heapify(nums)     # in place, O(n)
print(nums)             # [1, 2, 4, 3, 5, 9, 8]  ← same as your hand trace