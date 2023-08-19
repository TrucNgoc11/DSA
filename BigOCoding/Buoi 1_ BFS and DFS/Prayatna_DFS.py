import collections, sys
from typing import Dict, Tuple, DefaultDict
sys.setrecursionlimit(100002)


def solve() -> None:
	test_case = int(input())
	for _ in range(test_case):
		friend_num = int(input())
		m = int(input())
		gr = collections.defaultdict(list)
		for _ in range(m):
			u, v = map(int, input().split())
			gr[u].append(v)
			gr[v].append(u)
		print(helper(gr, friend_num))


def helper(gra, friend_num) -> int:
	ans = 0
	used = set()
	def dfs(cur) -> None:
		if cur in used:
			return
		used.add(cur)
		for ne in gra[cur]:
			dfs(ne)

	for i in range(friend_num):
		if i not in used:
			dfs(i)
			ans += 1

	return ans


solve()
