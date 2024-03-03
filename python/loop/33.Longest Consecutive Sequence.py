# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Step 1: Sort the input list in ascending order.
        nums.sort()

        # Step 2: Initialize variables 'maxLength' and 'currentLength' to 1.
        maxLength = 1
        currentLength = 1

        # Step 3: Iterate through the sorted array, starting from the second element.
        for i in range(1, len(nums)):
            # Step 4: Check if the current number is not equal to the previous one.
            if nums[i] != nums[i - 1]:
                # Step 5: If the current number is one more than the previous one, it is part of the consecutive sequence.
                if nums[i] == nums[i - 1] + 1:
                    currentLength += 1
                else:
                    # If not consecutive, reset the current length.
                    currentLength = 1

                # Step 6: Update the maximum length.
                maxLength = max(maxLength, currentLength)

        # Step 7: Return 'maxLength' as the length of the longest consecutive sequence.
        return maxLength