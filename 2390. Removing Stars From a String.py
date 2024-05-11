# https://leetcode.com/problems/removing-stars-from-a-string/
class Solution:
    def removeStars(self, s: str) -> str:
        # It's like hitting a backspace everytime we see a star
        # so whenever there's an operation to be done on the most recent element
        # stack is way to go
        stack = []
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
