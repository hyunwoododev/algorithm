# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):
            if total == target:
                result.append(curr[:])
                return
            
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return result