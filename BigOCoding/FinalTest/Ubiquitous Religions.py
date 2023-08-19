import collections
from typing import List


def bfs(gr, start, n):
	pool = [(start, 0)]
	used = set()
	used.add(start)
	ans = 0
	while pool:
		tmp = []
		for cur in pool:
			for ne in gr[cur]:
				if ne not in used:
					tmp.append(ne)
					used.add(ne)
		pool = tmp
		ans += 1
	return ans


def solve():
	n, m = map(int, input().split())
	gr = collections.defaultdict(list)
	for _ in range(m):
		u, v = map(int, input().split())
		gr[u].append(v)
		gr[v].append(u)
	print(gr, bfs, i )



solve()

