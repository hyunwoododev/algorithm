# https://leetcode.com/problems/last-stone-weight/description/

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            newS = (-s1)-(-s2)
            heapq.heappush(heap, -newS)
        return heap[0] * -1