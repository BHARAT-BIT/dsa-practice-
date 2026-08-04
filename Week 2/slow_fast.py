def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1


# --- Example usage ---
arr = [1, 1, 2, 2, 3, 4, 2, 4]

count = remove_duplicates(arr)

print("Full array after in-place shuffle:", arr)
print("Number of unique elements:", count)
print("Clean deduped array:", arr[:count])