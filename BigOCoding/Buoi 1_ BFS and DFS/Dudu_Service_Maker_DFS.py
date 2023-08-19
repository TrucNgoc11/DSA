import collections, sys
from typing import DefaultDict
sys.setrecursionlimit(100009)

VISITED = 0
UNVISIT = 1
PROCESSING = 2


def helper(gr, n) -> bool:
	#print(gr)
	color = [UNVISIT] * (n + 1)
	def dfs(cur):
		if color[cur] == VISITED:
			return False
		
		if color[cur] == PROCESSING:
			return True
		color[cur] = PROCESSING
		for ne in gr[cur]:
			if dfs(ne):
				return True
		color[cur] = VISITED
		return False

	for i in range(1, n + 1):
		if color[i] == UNVISIT and dfs(i):
			return True
	return False


def solve() -> None:
	test_case = int(input())
	for _ in range(test_case):
		gr = collections.defaultdict(list)
		n, m = map(int, input().split())
		for _ in range(m):
			u, v = map(int, input().split())
			gr[u]. append(v)
		if helper(gr, n):
			print("YES")
		else:
			print("NO")


solve()
