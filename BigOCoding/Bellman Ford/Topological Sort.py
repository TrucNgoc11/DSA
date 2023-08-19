import heapq
from typing import List


def topological_sort(graph, n) -> List[int]:
	in_degree = [0] * (n + 1)
	pool = []
	for u in range(1, n + 1):
		for v in graph[u]:
			in_degree[v] += 1
	for u in range(1, n + 1):
		if in_degree[u] == 0:
			pool.append(u)

	heapq.heapify(pool)

	ans = []
	while pool:
		u = heapq.heappop(pool)
		ans.append(u)
		for v in graph[u]:
			in_degree[v] -= 1
			if in_degree[v] == 0:
				heapq.heappush(pool, v)
	if len(ans) == n:
		return ans
	return []


def solve():
	n, m = map(int, input().split())
	graph = [[] for _ in range(n + 1)]
	for _ in range(m):
		u, v = map(int, input().split())
		graph[u].append(v)
	ans = topological_sort(graph, n)
	if ans:
		print(" ".join(str(x) for x in ans))
	else:
		print("Sandro fails.")


solve()

