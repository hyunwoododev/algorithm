# https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        stack = []

        def dfs(idx):
            if sum(stack) == target:
                res.append(stack[:])
                return
            
            if sum(stack) > target:
                return

            prev = -1
            for i in range(idx, len(candidates)):
                if prev == candidates[i]:
                    continue
                
                stack.append(candidates[i])
                dfs(i+1)
                stack.pop()
                prev = candidates[i]

        dfs(0)
        return res



