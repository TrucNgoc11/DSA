def solve():
	test_case = int(input())
	for x in range(1, 1 + test_case):
		h, w = map(int, input().split())
		matrix = []
		a = None
		for _ in range(w):
			matrix.append(input())
		for i in range(w):
			for j in range(h):
				if matrix[i][j] == "@":
					a = (i, j)
					break
			if a:
				break
		ans = bfs(matrix, a)
		print(f"Case {x}: {ans}")


def bfs(matrix, a):
	W, H = len(matrix), len(matrix[0])
	pool = [a]
	used = set(pool)
	ans = 0
	while pool:
		tmp = []
		for cur_x, cur_y in pool:
			ans += 1
			for ne_x, ne_y in [(cur_x - 1, cur_y), (cur_x + 1, cur_y), (cur_x, cur_y - 1), (cur_x, cur_y + 1)]:
				if not (0 <= ne_x < W and 0<= ne_y < H):
					continue
				if matrix[ne_x][ne_y] == "#":
					continue
				if (ne_x, ne_y) in used:
					continue
				tmp.append((ne_x, ne_y))
				used.add((ne_x, ne_y))
		pool = tmp
	return ans


solve()
