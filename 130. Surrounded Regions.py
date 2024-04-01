# https://leetcode.com/problems/surrounded-regions/description/
"""
every O connected to edge O should not be converted
so, find those and change everything else
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edgezero = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r<0 or c<0 or r==ROWS or c==COLS or (r,c) in edgezero or board[r][c] != 'O'):
                return
            
            edgezero.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c)

        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS-1] == 'O':
                dfs(r, COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in edgezero:
                    board[r][c] = 'X'
