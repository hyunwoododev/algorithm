# https://leetcode.com/problems/task-scheduler/description/

from collections import deque,Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # heap 
        heap =[-i for i in count.values()]
        heapq.heapify(heap)
        
        # q
        q = deque()
        time = 0
        while q or heap:
            if heap:
                value = heapq.heappop(heap) * -1
                value = value - 1
                if value > 0:
                    q.append((value, time+n))
            while q and q[0][1] <= time:
                heapq.heappush(heap,q.popleft()[0] * -1)     
            time+=1
        return time
