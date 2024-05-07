"""
https://school.programmers.co.kr/learn/courses/30/lessons/42628

https://ohgyun.com/615 <= 유용함
"""

import heapq

def solution(operations):
    heap = []
    for oper in operations:
        op, value = oper.split(" ")
        if op == "I":
            heapq.heappush(heap,int(value))
        elif len(heap) > 0 and op == "D":
            if value == "1":
                maxValue = heapq.nlargest(1,heap)[0]
                maxidx = heap.index(maxValue)
                heap.pop(maxidx)
            else:
                heapq.heappop(heap)
    
    if len(heap) == 0:
        return [0,0]
    else:
        return [
            heapq.nlargest(1,heap)[0],
            heap[0]     
        ]                         

                             