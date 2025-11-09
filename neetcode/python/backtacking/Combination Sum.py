# https://leetcode.com/problems/combination-sum/
# 시간복잡도 : O(n * 2^n)
# Sum 시간복잡도 : O(n) * 모든 경우의 조합 수 : O(2^n)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        stack = []
        def dfs(idx):
            if sum(stack) > target:
                return
            
            if sum(stack) == target:
                output.append(stack[:])
                return

            if idx == len(candidates):
                return

            # 해당 숫자를 뽑는경우
            stack.append(candidates[idx])
            dfs(idx)
            stack.pop()

            # 해당 숫자를 뽑지 않는 경우
            dfs(idx+1)

        dfs(0)
        return output

