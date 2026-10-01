import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
print(h)                    # [1, 5, 3]  ← it's a plain list, laid out as a heap
print(heapq.heappop(h))     # 1          ← the min
print(h[0])                 # peek at the min without removing: O(1)