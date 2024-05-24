# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        stack = []

        def dfs(idx):

            if idx == len(nums):
                res.append(stack[:])
                return

            # 고르는 경우 
            stack.append(nums[idx])
            dfs(idx+1)
            stack.pop()
            
            # 고르지 않는경우 
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            dfs(idx + 1)
        dfs(0)
        return res