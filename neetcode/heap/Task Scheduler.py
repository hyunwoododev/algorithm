# https://leetcode.com/problems/task-scheduler/description/

import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)  

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time # 모든 태스크가 완료되는 데 필요한 최소 시간 반환
