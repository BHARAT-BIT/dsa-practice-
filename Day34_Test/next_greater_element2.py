def nextGreaterElements2(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(2 * n - 1, -1, -1):
        curr = nums[i % n]

        while stack and stack[-1] <= curr:
            stack.pop()

        if i < n:
            if stack:
                ans[i] = stack[-1]

        stack.append(curr)

    return ans