# https://leetcode.com/problems/backspace-string-compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(hashed):
            hcount = 0
            ptr = len(hashed)-1
            nonhashed = ''
            while ptr >=0:
                if hashed[ptr] == '#':
                    hcount += 1
                elif hcount == 0:
                    nonhashed += hashed[ptr]
                else:
                    hcount -= 1
                ptr -= 1
            return nonhashed
        
        return process(s) == process(t)
# different approach -- rather than processing all at once and comparing, this time am comparing one valid char at a time

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s), len(t)

        def getNextValid(p, string):
            hashCount = 0
            while hashCount >= 0 and p >= 0:
                p -= 1
                if string[p] == '#':
                    hashCount += 1
                else:
                    hashCount -= 1
            return p

        while p1 >=0 and p2 >= 0:
            p1 = getNextValid(p1, s)
            p2 = getNextValid(p2, t)

            if p1 == p2 == -1: # end of strings
                return True

            # length mismatch or chars don't match
            if (p1 >=0 and p2 == -1) or (p2 >=0 and p1 == -1) or s[p1] != t[p2]:
                return False
        
        return True
