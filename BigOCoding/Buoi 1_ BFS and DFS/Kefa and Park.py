import collections


def is_leaf(gr, cur): #check dinh la
	return len(gr[cur]) == 1


def helper(gr, k, list_values):
	ans = 0
	used = set()
	def dfs(gr, cur, m, list_values, k):
		nonlocal ans
		if cur in used:
			return
		used.add(cur)
		if list_values[cur - 1] == 1:
			m -= 1
			if m < 0:
				return
		else:
			m = k
		if is_leaf(gr, cur) and cur != 1:
			ans += 1
			return
		for ne in gr[cur]:
			dfs(ne, m)
	dfs(1, k)


def solve():
	n, k = map(int, input().split()