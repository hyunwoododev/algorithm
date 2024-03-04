# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices):
        left = 0 
        right = 1 
        max_profit = 0
        while right < len(prices): 
            # 현재 단계 손익 계산
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]: 
                max_profit = max(currentProfit, max_profit) 
            # 산 가격이 판가격보다 작거나 같으면,
            else:
                left = right
                
            right += 1
        return max_profit
