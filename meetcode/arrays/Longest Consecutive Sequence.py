# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1
        
        nums.sort()
        maxRef = 1
        curr = 1

        # length of nums is over two 
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                curr = 1
            maxRef = max(maxRef, curr)

        return maxRef