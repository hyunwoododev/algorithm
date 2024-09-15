# https://leetcode.com/problems/k-closest-points-to-origin/description/

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answer = []
        heap = []
        pairs = [(i,x,y) for i,[x,y] in enumerate(points)]

        for pair in pairs:
            i,x,y = pair
            heapq.heappush(heap,((x-0)**2 + (y-0)**2,i))

        for i in range(k):
            m = heapq.heappop(heap)
            answer.append(points[m[1]])
            
        return answer