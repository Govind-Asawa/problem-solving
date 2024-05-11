# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for op in operations:
            if op == '+':
                a = s.pop()
                b = s.pop()
                s.append(b)
                s.append(a)
                s.append(a+b)
            elif op == 'C':
                s.pop()
            elif op == 'D':
                a = s[-1]
                s.append(a*2)
            else:
                s.append(int(op))
        
        return sum(s) if len(s) else 0
