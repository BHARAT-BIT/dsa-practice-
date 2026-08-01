def single_2(nums):
    ones = 0 
    twos = 0 
    for i in range(len(nums)):
        ones = (ones ^ nums[i]) & ~twos 
        twos = (twos ^ nums[i]) & ~ones 
    return ones 
    