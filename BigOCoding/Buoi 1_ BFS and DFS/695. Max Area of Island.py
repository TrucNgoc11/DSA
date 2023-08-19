from typing import List, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		n, m = len(grid), len(grid[0])
		def dfs(curx, cury, used):

			if (curx, cury) in used:
				return
			used.add((curx, cury))
			for (nex, ney) in [(curx + 1, cury), (curx - 1, cury), (curx, cury + 1), (curx, cury - 1)]:
				if not (0 <= nex < n and 0 <= ney < m):
					continue
				if grid[nex][ney] == "0":
					continue
				dfs(grid, nex, ney, used)


		def helper(grid):
			used = set()
			ans = set
			for i in range(n):
				for j in range(m):
					if grid[i][j] == 1 and (i, j) not in used:
						dfs(gri)