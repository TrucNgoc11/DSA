import collections


def solve():
	n = int(input())
	gr = collections.defaultdict(list)
	for _ in range(n - 1):
		u, v = map(int, input().split())
		gr[u].append(v)
		gr[v].append(u)
	girl_num = int(input())
	girl_list = [False] * (n + 1)
	for _ in range(girl_num):
		i = int(input())
		girl_list[i] = True
	print(bfs(1, gr, girl_list))


def bfs(a, gr, girl_list):
		t = 0
		pool = [a]
		used = set(pool)
		ans = depth_ans = 0
		while pool:
			tmp = []
			for cur in pool:
				if girl_list[cur]:
					if ans == 0 or (depth_ans > t) or (depth_ans == t and cur < ans):
						ans = cur
						depth_ans = t
					continue
				for ne in gr[cur]:
					if ne in used:
						continue
					tmp.append(ne)
					used.add(ne)
			pool = tmp
			t += 1
		return ans


solve()


