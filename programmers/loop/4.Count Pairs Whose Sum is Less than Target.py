# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1:
            return 0

        nums.sort()
        l = 0
        r = len(nums) - 1
        pairCount = 0

        while l <= r:
            if nums[l] + nums[r] >= target:
                r -= 1
            else:
               pairCount += r - l
               l += 1

        return pairCount
