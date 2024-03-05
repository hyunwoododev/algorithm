# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        answer = right

        while left <= right:  
            mid = (left + right) // 2
            total = 0
            for pile in piles:
                if pile % mid == 0:
                    total += pile // mid
                else:
                    total += (pile // mid) + 1  
            if total <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

            


        