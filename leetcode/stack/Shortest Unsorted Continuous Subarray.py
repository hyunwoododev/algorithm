# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        l, u = len(nums) - 1, 0
        stack = []
        
        # 왼쪽부터 시작해서 정렬이 깨지는 지점 찾기
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        
        stack = []
        
        # 오른쪽부터 시작해서 정렬이 깨지는 지점 찾기
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                u = max(u, stack.pop())
            stack.append(i)
        
        return 0 if l >= u else u - l + 1
