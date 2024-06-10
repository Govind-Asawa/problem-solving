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
