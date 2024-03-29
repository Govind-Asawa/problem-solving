# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def __init__(self):
        self.phonemap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        if len(digits) == 1:
            return list(self.phonemap[digits[0]])

        num = digits[0]
        dcopy =  digits[1:]

        ans = []
        combs = self.letterCombinations(dcopy)
        for char in self.phonemap[num]:
            for comb in combs:
                ans.append(char + comb)

        return ans
                
        
