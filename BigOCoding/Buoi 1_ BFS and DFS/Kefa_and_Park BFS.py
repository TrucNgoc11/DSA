import collections

def is_leaf(gr, cur):
	return len(gr[cur]) == 1


def bfs(gr, start, k, list_values):
	pool = [(start, k)]
	used = set(pool)
	ans = 0
	while pool:
		tmp = []
		for cur, m in pool:
			if list_values[cur - 1] == 1:
				m -= 1
				if m < 0:
					continue
			else:
				m = k
			if is_leaf(gr, cur) and cur != 1:
				ans += 1
			for ne in gr[cur]:
				if ne in used:
					continue
				used.add(ne)
				tmp.append((ne, m))
		pool = tmp
	return ans


def solve():
	n, k = map(int, input().split())
	list_values = list(map(int, input().split()))
	gr = collections.defaultdict(list)
	start = 1
	for i in range(n - 1):
		u, v = map(int, input().split())
		if u == v:
			continue
		gr[u].append(v)
		gr[v].append(u)
	print(bfs(gr, start, k, list_values))


solve()