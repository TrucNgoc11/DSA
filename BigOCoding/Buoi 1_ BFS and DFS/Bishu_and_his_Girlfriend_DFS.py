import collections


def solve():
	n = int(input())
	gr = collections.defaultdict(list)
	for _ in range(n - 1):
		u, v = map(int, input().split())
		gr[u].append(v)
		gr[v]. append(u)
	girl_nums = int(input())
	girl_list = [False] * (n + 1)
	for _ in range(girl_nums):
		i = int(input())
		girl_list[i] = True
	print(helper(gr, girl_list))


def helper(gr, girl_list):
	ans = depth_ans = 0
	used = set()
	def dfs(cur, depth):
		nonlocal ans, depth_ans
		if cur in used:
			return
		used.add(cur)
		if girl_list[cur] is True:
			if ans == 0 or (depth_ans > depth) or (depth_ans == depth and cur < ans):
				depth_ans = depth
				ans = cur
			return
		for ne in gr[cur]:
			dfs(ne, depth + 1)

	dfs(1,0)
	return ans


solve()