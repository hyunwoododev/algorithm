# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        answer = None
        while heap and k > 0:
            answer = heapq.heappop(heap)
            k -= 1
        return answer * -1