def missing_number(nums):
    n = len(nums)
    result = 0
    for num in nums:
        result ^= num
    for i in range(n + 1):
        result ^= i
    return result