"""
There are n teams numbered from 0 to n - 1 in a tournament.
Given a 0-indexed 2D boolean matrix grid of size n * n. For all i, j that 0 <= i, j <= n - 1 and i != j team i is stronger than team j if grid[i][j] == 1, otherwise, team j is stronger than team i.
Team a will be the champion of the tournament if there is no team b that is stronger than team a.
Return the team that will be the champion of the tournament.

Example 1:
Input: grid = [[0,1],[0,0]]
Output: 0
Explanation: There are two teams in this tournament.
grid[0][1] == 1 means that team 0 is stronger than team 1. So team 0 will be the champion.
"""
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        return self.v2(grid)
        
        
    def v1(self, grid):
        """
        Time: O(n^2)
        Space: O(1)
        """
        n = len(grid)
        for i in range(n):
            if sum(grid[i]) == n - 1:
                return i
    def v2(self, grid):
        n = len(grid)
        for i in range(n):
            flag = True
            for j in range(n):
                if i != j and grid[i][j] == 0:
                    flag = False
            if flag:
                return i
        return -1
