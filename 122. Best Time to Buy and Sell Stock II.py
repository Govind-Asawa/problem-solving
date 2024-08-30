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

# Another try
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]

        return profit   
