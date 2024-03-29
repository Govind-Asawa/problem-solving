"""
'+' means append to all the lists returned
"aabbaa"=-> [a] + part(abbaa),
            -> [a] + part(bbaa)
                -> [b] + part(baa)
                    -> [b] + part(aa)
                        -> [a] + part(a)
                        -> [aa] + part('')
            -> [abba] + part(a)
                -> [a] + part('')
          
          -> [aa] + part(bbaa),
            -> [b] + part(baa)
                -> [b] + part(aa)
                    -> [a] + part(a)
                    -> [aa] + part('')
            -> [bb] + part(aa)
          
          -> aabbaa + part('')

Since there are a lot of overlapping subproblems, used dp
"""

class Solution:
    def isPalin(self, substr):
        return substr == substr[::-1]

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = dict()
        
        return self.palins(0, dp, n, s)
        
    def palins(self, idx, dp, n, s):
        if idx == n:
            return [[]]
        
        if idx in dp:
            return dp[idx]

        palindromeList = []
        for i in range(idx, n):
            if self.isPalin(s[idx:i+1]):
                for subPalin in self.palins(i+1, dp, n, s):
                    palindromeList.append([s[idx:i+1]] + subPalin)
        
        dp[idx] = palindromeList
        return palindromeList
