# https://leetcode.com/problems/fruit-into-baskets/description/
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # (most recent idx, fruit type)
        bas1, bas2 = [0, fruits[0]], [-1, -1]
        count, maxc = 0, 0
        start, end = 0, 0

        while end < len(fruits):
            f = fruits[end]
            if bas1[1] != f and bas2[1] != f: # new fruit
                if fruits[end-1] == bas1[1]: #so put the new f in basket 2
                    start = bas2[0]+1 #reset start to fruit2's most recent + 1, coz from there to end we'll only have fruit1
                    bas2[1] = f # put the new fruit in basket 2
                    bas2[0] = end
                else:
                    start = bas1[0]+1
                    bas1[1] = f # put the new fruit in basket 2
                    bas1[0] = end
                
                maxc = max(maxc, count)
                count = end - start + 1
                
            else:
                count += 1
                if f == bas1[1]:
                    bas1[0] = end
                else:
                    bas2[0] = end
                
            end += 1
    
        return max(maxc, count)
