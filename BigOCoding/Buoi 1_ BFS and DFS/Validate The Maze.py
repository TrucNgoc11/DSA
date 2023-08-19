def solve():
	test_case = int(input())
	for _ in range(test_case):
		n, m = map(int, input().split()) #n: so hang row, m: so cot column
		matrix = []
		for _ in range(n):
			matrix.append(input())
		candi = set()
		for i in range(n):
			if matrix[i][0] == ".":
				candi.add((i, 0))
			if matrix[i][m - 1] == ".":
				candi.add((i, m - 1))
		for j in range(m):
			if matrix[0][j] == ".":
				candi.add((0, j))
			if matrix[n-1][j] == ".":
				candi.add((n - 1, j))
	#	print(candi)
		candi = list(candi)
		if len(candi) != 2:
			print("invalid")
		else:
			if bfs(matrix, candi[0], candi[-1]):
				print("valid")
			else:
				print("invalid")


def bfs(matrix, a, b):
	n, m = len(matrix), len(matrix[0])
	pool = [a]
	used = set(pool)
	while pool:
		tmp = []
		for cur_x, cur_y in pool:
			if (cur_x, cur_y) == b:
				return True
			for ne_x, ne_y in [(cur_x - 1, cur_y), (cur_x + 1, cur_y), (cur_x, cur_y - 1), (cur_x, cur_y + 1)]:
				if not (0 <= ne_x < n and 0 <= ne_y < m):
					continue
				if matrix[ne_x][ne_y] == "#":
					continue
				if (ne_x, ne_y) in used:
					continue
				tmp.append((ne_x, ne_y))
				used.add((ne_x, ne_y))
		pool = tmp
	return False


solve()
