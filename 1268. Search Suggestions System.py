# https://leetcode.com/problems/search-suggestions-system/
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prev = sorted(products)
        current, ans = [], []

        for i in range(len(searchWord)):
            for prd in prev:
                if len(prd) > i and prd[i] == searchWord[i]:
                    current.append(prd)
            
            if len(current) < 3:
                ans.append(current[:])
            else:
                ans.append(current[:3])
            
            prev = current
            current = []

        return ans
