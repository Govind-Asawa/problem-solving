# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        combined = (s1 + ' ' + s2).split()
        result = set()
        duplicate = set()
        for word in combined:
            if word not in result:
                result.add(word)
            else:
                duplicate.add(word)
        return result - duplicate
