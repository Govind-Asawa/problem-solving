# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0
        cp = 10001

        for p in prices:
            if cp > p:
                cp = p
            else:
                tot += p - cp
                cp = p
        
        return tot
