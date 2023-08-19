def solve():
	n, m = map(int, input().split())
	ma = []
	for _ in range(n):
		ma.append(input())
	used = set()
	cuu = soi = 0
	for i in range(n):
		for j in range(m):
			if ma[i][j] == "#":
				continue
			if (i, j) in used:
				continue
			ans = bfs(i, j, ma, used)
			cuu += ans[0]
			soi += ans[1]

	print(f"{cuu} {soi}")


def bfs(x, y, ma, used):
	n, m = len(ma), len(ma[0])
	pool = [(x, y)]
	used.add((x, y))
	cuu = 0
	soi = 0
	is_round = True
	while len(pool) > 0:
		tmp = []
		for idx, idy in pool:
			if ma[idx][idy] == "k":
				cuu += 1
			if ma[idx][idy] == "v":
				soi += 1
			for (ne_x, ne_y) in [(idx - 1, idy), (idx + 1, idy), (idx, idy + 1), (idx, idy - 1)]:
				if (ne_x, ne_y) in used:
					continue
				if not (0 <= ne_x < n and 0 <= ne_y < m):
					is_round = False
					continue
				if ma[ne_x][ne_y] == "#":
					continue
				tmp.append((ne_x, ne_y))
				used.add((ne_x, ne_y))
		pool = tmp

	if not is_round:
		return (cuu, soi)

	if cuu <= soi:
		cuu = 0
	else:
		soi = 0

	return (cuu, soi)


solve()







