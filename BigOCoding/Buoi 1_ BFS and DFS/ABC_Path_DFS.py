def helper(ma, i, j):
	n, m = len(ma), len(ma[0])
	ans = 0
	def dfs(curx, cury, depth):
		nonlocal ans
		ans = max(ans, depth)
		for nex, ney in [(curx + 1, cury), (curx - 1, cury), (curx, cury + 1), (curx, cury - 1), (curx + 1, cury + 1), (curx - 1, cury - 1), (curx - 1, cury + 1), (curx + 1, cury - 1)]:
			if not ((0 <= nex < n) and (0 <= ney < m)):
				continue
			if (ord(ma[curx][cury]) - ord(ma[nex][ney])) != -1:
				continue
			dfs(nex, ney, depth + 1)
	dfs(i, j, 1)
	return ans


def solve():
	case = 0
	while True:
		n, m = map(int, input().split())
		if n == m == 0:
			break
		ma = []
		for _ in range(n):
			ma.append(input())
		ans = 0
		for i in range(n):
			for j in range(m):
				if ma[i][j] != "A":
					continue
				ans = max(ans, helper(ma, i, j))
		case += 1
		print(f"Case {case}: {ans}")


solve()


