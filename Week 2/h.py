arr = [3, 1, 4, 1, 5, 9, 2]

current_max = float('-inf')   # starts at "negative infinity" so anything beats it
for num in arr:
    if num > current_max:
        current_max = num
    print(f"Looking at {num}, max so far is {current_max}")