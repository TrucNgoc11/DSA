import heapq
from typing import List

MAX_SIZE = 3


def helper(array) -> List[int]:
	ans = []
	pool = []
	for val in array:
		heapq.heappush(pool, val)
		if len(pool) > MAX_SIZE:
			heapq.heappop(pool)
		if len(pool) == MAX_SIZE:
			ans.append(pool[0] * pool[1] * pool[2])
		else:
			ans.append(-1)
	return ans


def solve() -> None:
	_ = int(input())
	array = list(map(int, input().split()))
	ans = helper(array)
	for i in ans:
		print(i)


solve()