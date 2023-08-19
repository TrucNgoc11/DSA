import collections
from typing import DefaultDict


def helper(gr: DefaultDict, start: int) -> int:
	used = set()
	def bfs(cur) -> None:
		pool = [cur]
		used.add(cur)
		while pool:
			tmp = []
			for cur in pool:
				for ne in gr[cur]:
					if ne in used:
						continue
					tmp.append(ne)
					used.add(ne)
			pool = tmp
	bfs(start)
	return len(used)


def solve() -> None:
	bom_num, m = map(int, input().split())
	gr = collections.defaultdict(list)
	for _ in range(m):
		u, v = map(int, input().split())
		if u == v:
			continue
		gr[u].append(v)
	ans = 0
	for i in range(bom_num):
		ans = max(ans, helper(gr, i + 1))
	print(ans)


solve()