# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxNum = 1
        curr = 1
        nums.sort()
        
        if len(nums) < 1:
            return 0

        for idx in range(1,len(nums)):
            if nums[idx-1] + 1 == nums[idx]:
                curr += 1
            elif nums[idx-1] == nums[idx]:
                continue
            else:
                curr = 1
            maxNum = max(maxNum, curr)
        return maxNum

