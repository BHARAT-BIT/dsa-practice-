def single_3(nums):
    xor = 0 
    unique1 = 0 
    unique2 = 0 
    for i in range(len(nums)):
        xor = xor ^ nums[i]
    rightmost =  xor & ~(xor -1)
    for i in range(len(nums)):
        if nums[i] & rightmost != 0:
            unique1 = unique1 ^ nums[i]
        else:    
            unique2 = unique2 ^ nums[i]
    return [unique1,unique2]        