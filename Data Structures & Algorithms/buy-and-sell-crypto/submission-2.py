class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyPrice = prices[0]
        maxProfit = 0

        for sellPrice in prices[1:]:

            if buyPrice < sellPrice:
                maxProfit = max(maxProfit, sellPrice - buyPrice)
            else:
                buyPrice = sellPrice # update to new minimum number


        return maxProfit