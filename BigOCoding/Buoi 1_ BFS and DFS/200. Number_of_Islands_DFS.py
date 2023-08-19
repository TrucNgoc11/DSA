from typing import List, Tuple, Set
class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		def dfs(grid: List[List[str]], curx: int, cury: int, used: Set) -> None:
			n, m = len(grid), len(grid[0])
			if (curx, cury) in used:
				return
			used.add((curx, cury))
			for (nex, ney) in [(curx + 1, cury), (curx - 1, cury), (curx, cury + 1), (curx, cury - 1)]:
				if not (0 <= nex < n and 0 <= ney < m):
					continue
				if grid[nex][ney] == "0":
					continue
				dfs(grid, nex, ney, used)


		def helper(grid: List[List[str]]) -> int:
			used = set()
			n, m = len(grid), len(grid[0])
			ans = 0
			for i in range(n):
				for j in range(m):
					if grid[i][j] == "1" and (i, j) not in used:
						dfs(grid, i, j, used)
						ans += 1
			return ans

		return helper(grid)









