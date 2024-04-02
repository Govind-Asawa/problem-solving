# https://leetcode.com/problems/isomorphic-strings/description/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps, mapt = {}, {}

        for cs, ct in zip(s,t):
            if (cs in maps and maps[cs] != ct) or (ct in mapt and mapt[ct] != cs):
                return False
            
            maps[cs] = ct
            mapt[ct] = cs

        return True
