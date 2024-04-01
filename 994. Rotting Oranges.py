# https://leetcode.com/problems/rotting-oranges/description/
# simple optimization could be to keep track of no of fresh oranges, if zero in the end, return time else -1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        time = 0
        dirs = [0, 1, 0, -1, 0]
        m,n = len(grid), len(grid[0])

        def valid(r, c):
            if r<0 or c<0 or r==m or c==n:
                return False
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
        
        while q:
            size = len(q)
            for _ in range(size):
                r,c = q.pop(0)
                for i in range(4):
                    nr, nc = r+dirs[i], c+dirs[i+1]
                    if valid(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr,nc])
            if q:  #if rotten oranges were added
                time += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time
