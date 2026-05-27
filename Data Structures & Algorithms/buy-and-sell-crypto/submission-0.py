# [10, 1, 5, 6, 7, 1], MP = -inf, CP = 0
#  ^           ^
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minBuy = float("inf")
        for price in prices:
            maxProfit = max(maxProfit, price - minBuy)
            minBuy = min(minBuy, price) 
        
        return maxProfit