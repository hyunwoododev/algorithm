# https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # n-1 탐색이 만약에 리스트였다면 O(N)인데 set이어서 n-1 찾는게 O(1)
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
                
        return longest
