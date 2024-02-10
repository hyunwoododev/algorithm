"""
https://school.programmers.co.kr/learn/courses/30/lessons/42626
"""
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        else:
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
            answer += 1
    return answer

