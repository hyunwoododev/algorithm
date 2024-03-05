# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        l = 0 
        r = 1 
        while r < len(prices): 
            # 현재 단계 손익 계산
            currentProfit = prices[r] - prices[l]
            if prices[l] < prices[r]: 
                max_profit = max(currentProfit, max_profit)
                
            # 산 가격이 판가격보다 작거나 같으면, 산가격 업데이트
            else:
                l = r
                
            r += 1
        return max_profit
