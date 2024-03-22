# https://leetcode.com/problems/house-robber/description/

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # nums가 하나 일때 
#         if len(nums) == 1:
#             return nums[0]
            
#         #nums가 하나 이상 일때
#         dp = [0] * (len(nums))     
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1]) 

#         for i in range(2, len(nums)):
#             dp[i] = max(dp[i-2] + nums[i], dp[i-1]) 

#         return dp[len(nums)-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
