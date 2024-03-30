# https://leetcode.com/problems/max-area-of-island/description/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.rDir = [0, 1, 0, -1]
        self.cDir = [1, 0, -1, 0]
        self.grid = grid
        self.visited = [[False] * n for _ in range(m)]

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not self.visited[i][j]:
                    maxArea = max(maxArea, self.dfs(i, j, m, n))
                    
        return maxArea

    def dfs(self, r, c, m, n):
        self.visited[r][c] = True
        area = 1

        for i in range(4):
            nr = r + self.rDir[i]
            nc = c + self.cDir[i]

            if (
                self.valid(nr, nc, m, n)
                and not self.visited[nr][nc]
                and self.grid[nr][nc]
            ):
                area += self.dfs(nr, nc, m, n)
        
        return area

    def valid(self, r, c, m, n):
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        return True
