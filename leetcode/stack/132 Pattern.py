# https://leetcode.com/problems/132-pattern/description/

class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        
        stack = []
        second = float('-inf')
        
        for num in reversed(nums):
            if num < second:
                return True
                
            while stack and stack[-1] < num:
                second = stack.pop()
            stack.append(num)
        
        return False
