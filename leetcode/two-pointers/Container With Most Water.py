# https://leetcode.com/problems/container-with-most-water/description/
# ⭐️

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l)) # 가로조심 연산순서바뀐다
            if height[l] <= height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            
        return res
