# https://leetcode.com/problems/combination-sum-ii/description/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 후보 정렬
        res = []  # 결과를 저장할 리스트

        def dfs(idx, stack, current_sum):
            if current_sum == target:  # 타겟 값에 도달했으면 결과에 추가
                res.append(stack[:])
                return
            
            for i in range(idx, len(candidates)):
                # 중복된 요소 건너뛰기
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                # 현재 합에 후보를 추가했을 때 타겟 값을 초과하면 더 이상 탐색하지 않음
                if current_sum + candidates[i] > target:
                    break
                
                # 다음 요소로 DFS 수행
                dfs(i+1, stack + [candidates[i]], current_sum + candidates[i])

        dfs(0, [], 0)
        return res

