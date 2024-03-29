# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = [] 

        def dfs():
            if len(stack) == len(nums):
                res.append(stack[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in stack:
                    stack.append(nums[i])
                    dfs()
                    stack.pop()
        dfs()
        return res