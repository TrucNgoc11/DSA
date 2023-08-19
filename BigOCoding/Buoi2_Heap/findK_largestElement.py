import heapq

k = 5
pool = []
nums = [1, 3, 2, 8, 5, 15, 12]
for val in nums:
	pool.append(-val)
heapq.heapify(pool)
for _ in range(4):
	heapq.heappop(pool)

print(pool)