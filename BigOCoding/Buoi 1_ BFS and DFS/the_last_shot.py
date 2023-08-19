import collections, sys
from typing import DefaultDict
sys.setrecursionlimit(10009)

def helper(gr: DefaultDict, start: int, n: int) -> int:
	used = [False] * (n + 1)
	count = 0
	def dfs(cur):
		nonlocal count
		used[cur] = True
		count += 1
		for ne in gr[cur]:
			if used[ne]:
				continue
			dfs(ne)
	dfs(start)
	return count


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
		ans = max(ans, helper(gr, i + 1, bom_num))
	print(ans)


solve()




