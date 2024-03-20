# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1 
        curr_min = float("inf")
        
        while l  <=  r :
            mid = l + (r - l ) // 2
            curr_min = min(curr_min, nums[mid]) # mid값이 최소일수있으니.
            
            # right has the min 
            if nums[mid] > nums[r]:
                l = mid + 1
                
            # left has the  min 
            else:
                r = mid - 1 
                
        return min(curr_min,nums[l])
