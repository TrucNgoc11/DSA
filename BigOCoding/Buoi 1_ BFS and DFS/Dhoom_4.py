MOD = 100000


def bfs(a, b, list_values):
	pool = [a]
	used = [False] * 100001
	used[a] = True
	t = 0
	while pool:
		tmp = []
		for cur in pool:
			if cur == b:
				return t
			for k in list_values:
				ne = (cur * k) % MOD
				if used[ne]:
					continue
				tmp.append(ne)
				used[ne] = True
		pool = tmp
		t += 1
	return -1


def solve():
	a, b = map(int, input().split())
	_ = int(input())
	list_values = list(map(int, input().split()))
	print(bfs(a, b, list_values))


solve()