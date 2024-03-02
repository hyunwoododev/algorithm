# https://leetcode.com/problems/permutations/description/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(stack, res):
            if len(stack) == len(nums):
                res.append(stack[:])
                return

            for i in nums:
                if i not in stack:
                    stack.append(i)
                    dfs(stack,res)
                    stack.pop()
 
        response = []
        dfs([],response) 
        return response
        