# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        # 제일작은게 + 이면 바로 -1리턴
        if nums[0] >= 0:
            return -1
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] >= 0:
                return -1
            
            if nums[i] == -nums[j]:
                return nums[j]
            
            if nums[i] < -nums[j]:
                j-=1
                
            else:
                i+=1

        return -1