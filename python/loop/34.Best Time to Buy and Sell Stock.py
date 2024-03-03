# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices):
        left = 0  # 'left'는 구매할 날짜를 가리키는 인덱스입니다.
        right = 1  # 'right'는 판매할 날짜를 가리키는 인덱스입니다.
        max_profit = 0  # 최대 이익을 저장하는 변수입니다.
        while right < len(prices):  # 'right' 인덱스가 prices 배열의 길이를 넘지 않을 때까지 반복합니다.
            currentProfit = prices[right] - prices[left]  # 현재 이익을 계산합니다.

            if prices[left] < prices[right]:  # 구매가격이 판매가격보다 낮은 경우,
                max_profit = max(currentProfit, max_profit)  # 최대 이익을 업데이트합니다.

            else:  # 구매가격이 판매가격보다 높거나 같은 경우,
                left = right  # 구매 날짜를 현재 'right' 위치로 업데이트합니다.
                
            right += 1  # 판매 날짜를 다음 날로 이동합니다.
        return max_profit  # 계산된 최대 이익을 반환합니다.
