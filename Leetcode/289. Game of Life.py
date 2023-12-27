"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

EX1: 
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.v2_savespace(board)
    def v1(self, board):
        """
        1. Make a copy original board
        2. Iterate the cells of the Board one by one.
        3. While computing the results of the rules, use the copy board and apply the result in the original board.
        Time: O(m * n)
        Space: O(m * n) because of copy board from original board
        """
        rows = len(board)
        cols = len(board[0])
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        neighbors = [(1, 0), (0, 1), (1, -1), (0, -1), (-1, -1), (-1, 1), (-1, 0),(1, 1)]

        for r in range(rows):
            for c in range(cols):
                # For each cell count the number of live neighbors.
                live_neigh = 0
                for neighbor in neighbors:
                    ne_row = r + neighbor[0]
                    ne_col = c + neighbor[1]
                    if (ne_row < rows and ne_row >= 0) and (ne_col < cols and ne_col >= 0) and (copy_board[ne_row][ne_col]== 1):
                        live_neigh += 1
                #Rule 1 and Rule 3
                if copy_board[r][c] == 1 and (live_neigh < 2 or live_neigh > 3):
                    board[r][c] = 0
                #Rule 4
                if copy_board[r][c] == 0 and live_neigh == 3:
                    board[r][c] = 1
    def v2_savespace(self, board):
        """
        1. Iterate the cells of the Board one by one.
        2. The rules are computed and applied on the original board. The updated values signify both previous and updated value.
        3. Apply the updated rules to original board
         + Rule 1 change to - 1
         + Rule 2 no change
         + Rule 3 as rule 1 change to -1
         + rule 4 change to 2
        4.  iterate the board again and change the value to 1 if its value currently is greater than 0, and change the value to a 0 if its current value is lesser than or equal to 0.
        Time: O(m * n)
        Space: O(1)
        """
        rows = len(board)
        cols = len(board[0])
       
        neighbors = [(1, 0), (0, 1), (1, -1), (0, -1), (-1, -1), (-1, 1), (-1, 0),(1, 1)]

        for r in range(rows):
            for c in range(cols):
                # For each cell count the number of live neighbors.
                live_neigh = 0
                for neighbor in neighbors:
                    ne_row = r + neighbor[0]
                    ne_col = c + neighbor[1]
                    if (ne_row < rows and ne_row >= 0) and (ne_col < cols and ne_col >= 0) and abs(board[ne_row][ne_col]) == 1:
                        live_neigh += 1
                #Rule 1 and Rule 3
                if board[r][c] == 1 and (live_neigh < 2 or live_neigh > 3):
                    board[r][c] = -1
                #Rule 4
                if board[r][c] == 0 and live_neigh == 3:
                    board[r][c] = 2
        #Iterate again
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
        

        

        
