# https://leetcode.com/problems/combination-sum-ii/description/

# 시간복잡도 : O(n * 2^n)
# Sum 시간복잡도 : O(n) * 모든 경우의 조합 수 : O(2^n)

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
