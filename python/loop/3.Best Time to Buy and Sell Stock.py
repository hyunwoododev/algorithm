# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        buy = prices[0]
        sell = 0
        maxProfit = 0
        for idx in range(len(prices)):
            currentValue = prices[idx]
            if buy == currentValue:
                continue

            if buy > currentValue:
                buy = currentValue
                continue
            
            if buy < currentValue:
                maxProfit = max(maxProfit, currentValue-buy)
        return maxProfit
        



            
