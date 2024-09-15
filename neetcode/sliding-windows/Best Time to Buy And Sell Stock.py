# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for r in range(1, len(prices)):
            if prices[r] > buy:
                maxProfit = max(prices[r] - buy, maxProfit)
            else:
                buy = prices[r]
        return maxProfit
