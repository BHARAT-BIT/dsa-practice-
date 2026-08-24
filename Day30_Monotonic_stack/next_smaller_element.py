def nextSmallerElement(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    # Traverse from right to left
    for i in range(n - 1, -1, -1):

        # Remove elements greater than or equal to current
        while stack and stack[-1] >= nums[i]:
            stack.pop()

        # Top is the next smaller element
        if stack:
            result[i] = stack[-1]

        # Add current element
        stack.append(nums[i])

    return result