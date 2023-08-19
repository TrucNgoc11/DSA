import collections


def solve():
	test_case = int(input())
	for _ in range(test_case):
		n, m = map(int, input().split())
		gra = collections.defaultdict(list)
		for _ in range(m):
			u, v = map(int, input().split())
			gra[u].append(v)
			gra[v].append(u)
		start = int(input())
		ans = bfs(gra, start, n)
		tmp = [str(val) for idx, val in enumerate(ans) if idx not in (0, start)]
		ans = tmp
		print(" ".join(ans))


def bfs(gra, start, n):
	pool = [(start, 0)]
	ans = [-1] * (n + 1)
	used = set()
	used.add(start)
	while pool:
		tmp = []
		for cur, length in pool:
			ans[cur] = length
			for ne in gra[cur]:
				if ne not in used:
					tmp.append((ne, 6 + length))
					used.add(ne)
		pool = tmp
	return ans

solve()