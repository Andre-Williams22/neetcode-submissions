class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0 
        buyPrice = prices[0]

        for sellPrice in prices[1:]:

            if sellPrice > buyPrice:
                maxProfit = max(maxProfit, sellPrice - buyPrice)
            else:
                buyPrice = sellPrice

        return maxProfit
