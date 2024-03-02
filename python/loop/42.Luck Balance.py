# https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true

import heapq

N, K = map(int, input().strip().split())
loseTotal = 0
heap = []
for i in range(N):
    amount, importance = map(int, input().split())
    if importance == 0:
        loseTotal += amount
    else:
        heapq.heappush(heap, amount)
         
totalHeap = sum(heap)
lenHeap = len(heap)
i = 0
while i < lenHeap - K:
    totalHeap -= heapq.heappop(heap) * 2
    i += 1

print(loseTotal+totalHeap)