# [10, 1, 5, 6, 7, 1], MP = -inf, CP = 0
#         R
#      L
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                cp = prices[r] - prices[l]
                maxProfit = max(maxProfit, cp)
            else:
                l = r 
            r += 1 
        return maxProfit