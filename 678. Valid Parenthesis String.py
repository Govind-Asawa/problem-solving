# https://leetcode.com/problems/valid-parenthesis-string/description/
class Solution:
    def checkValidString(self, s: str) -> bool:
        openSt, starSt = [], []

        for i, c in enumerate(s):
            if c == '(':
                openSt.append(i)
            elif c == '*':
                starSt.append(i)
            elif openSt:
                openSt.pop()
            elif starSt:
                starSt.pop()
            else:
                return False

        for idx in openSt[::-1]:
            # A star can match an open bracket only if it comes after that bracket
            if not starSt or idx > starSt[-1]:
                return False
            starSt.pop()

        return True
