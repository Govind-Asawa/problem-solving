# https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.rDir = [0, 1, 0, -1]
        self.cDir = [1, 0, -1, 0]
        self.grid = grid
        self.visited = [[False] * n for _ in range(m)]

        nIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not self.visited[i][j]:
                    self.dfs(i, j, m, n)
                    nIslands += 1
        return nIslands

    def dfs(self, r, c, m, n):
        self.visited[r][c] = True

        for i in range(4):
            nr = r + self.rDir[i]
            nc = c + self.cDir[i]

            if (
                self.valid(nr, nc, m, n)
                and (not self.visited[nr][nc])
                and (self.grid[nr][nc] == "1")
            ):
                self.dfs(nr, nc, m, n)

    def valid(self, r, c, m, n):
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True
