# https://leetcode.com/problems/search-suggestions-system/
# two pointer approach: faster
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        sp = sorted(products)
        start, end = 0, len(products)-1
        ans = []

        for i in range(len(searchWord)):
            while start <= end and (len(sp[start]) <= i or sp[start][i] != searchWord[i]):
                start += 1

            while end >= start and (len(sp[end]) <= i or sp[end][i] != searchWord[i]):
                end -= 1

            if start > end:
                ans.append([])
            
            else:
                ans.append(sp[start: min(start+3, end+1)])    

        return ans
