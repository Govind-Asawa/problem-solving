# https://leetcode.com/problems/reverse-words-in-a-string-iii
class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = list(s.split())
        for i in range(len(sentence)):
            sentence[i] = sentence[i][::-1]
        
        return " ".join(sentence)
