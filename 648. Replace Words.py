# https://leetcode.com/problems/replace-words
class Solution_0:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dic = sorted(dictionary)
        ans = ""

        for word in sentence.split():
            found = False
            for dicword in dic:
                if word.startswith(dicword):
                    ans += dicword + " "
                    found = True
                    break
            if not found:
                ans += word + " "
        
        return ans[:-1]

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dicSet = set(dictionary)
        sentence = sentence.split()

        for i, word in enumerate(sentence):
            #check if any part of the word is in the set, replace the word with matched root
            # else leave it the way it was
            for j in range(1,len(word)+1):
                if word[:j] in dicSet:
                    sentence[i] = word[:j]
                    break

        return " ".join(sentence)
