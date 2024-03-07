# https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
import heapq

from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 각 작업의 빈도수를 계산합니다.
        count = Counter(tasks)
        # 최대 힙을 사용하여 가장 빈도수가 높은 작업부터 처리할 수 있도록 합니다.
        # 힙에는 각 작업의 빈도수의 음수 값을 저장하여 최대 힙을 구현합니다.
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # 전체 시간을 추적합니다.
        time = 0
        # 쿨다운 중인 작업을 추적하는 큐입니다.
        q = deque()
        while maxHeap or q:
            time += 1

            # 현재 처리할 수 있는 작업이 없으면, 쿨다운이 끝나는 다음 시간으로 점프합니다.
            if not maxHeap:
                time = q[0][1]
            else:
                # 가장 빈도수가 높은 작업을 처리합니다.
                cnt = 1 + heapq.heappop(maxHeap)
                # 작업이 여전히 남아있으면, 쿨다운을 고려하여 큐에 다시 추가합니다.
                if cnt:
                    q.append([cnt, time + n])
                    
            # 쿨다운이 끝난 작업을 다시 최대 힙에 추가합니다.
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        # 모든 작업을 완료하는 데 필요한 전체 시간을 반환합니다.
        return time

