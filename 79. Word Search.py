# https://leetcode.com/problems/word-search/description/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rDir = [0, 1, 0, -1]
        cDir = [1, 0, -1, 0]
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]

        def valid(r, c):
            if r<0 or c < 0 or r >= m or c>= n:
                return False
            return True

        def dfs(idx, r, c):
            if idx == len(word):
                return True
            
            if board[r][c] != word[idx]:
                return False

            # meaning it matched
            visited[r][c] = True

            for i in range(4):
                nr = r + rDir[i]
                nc = c + cDir[i]

                if (not valid(nr, nc) or visited[nr][nc]):
                    continue
                elif (dfs(idx+1, nr, nc)): #if total match found along this path
                    return True
            
            visited[r][c] = False
            # for cases like : [["a", "b", "c"]] and word = "abc"
            return (idx == len(word)-1) or False
        
        for i in range(m):
            for j in range(n):
                if(dfs(0, i, j)):
                    return True
                
        return False
