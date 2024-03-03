# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        maxLength = 1
        currentLength = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    currentLength += 1
                else:
                    maxLength = max(maxLength, currentLength)  # 여기로 이동
                    currentLength = 1

        return max(maxLength, currentLength)  # 마지막 비교를 위해 반복문 바깥으로 이동

