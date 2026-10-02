import heapq

nums = [5, 3, 8]
h = []
for x in nums:
    heapq.heappush(h, -x)       # negate on the way in

largest = -heapq.heappop(h)     # negate on the way out
print(largest)                  # 8