# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1dic, s2dic = {}, {}
        n1, n2 = len(s1), len(s2)

        for i in range(n1):
            s1dic[s1[i]] = s1dic.get(s1[i], 0)+1
            s2dic[s2[i]] = s2dic.get(s2[i], 0)+1
        
        start, end = 0, n1-1

        def check(d1, d2):     
            for k, v in d1.items():
                if d2.get(k, 0) != v:
                    return False
            
            return True

        while end < n2:
            if check(s1dic, s2dic):
                return True
            end += 1
            if end < n2:
                s2dic[s2[start]] -= 1
                s2dic[s2[end]] = s2dic.get(s2[end], 0) + 1
            start += 1
        
        return False
