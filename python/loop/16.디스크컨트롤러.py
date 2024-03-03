"""
https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""
import heapq

def solution(jobs):
    answer = 0
    #처리해야할 job의 갯수
    jobCnt = len(jobs)
    #처리된 job의 갯수
    completedCnt = 0
    heap = []
    now = 0  
    completedTime= -1
    
    while jobCnt > completedCnt:
        #처리해야할 job들을 추가하는 배열.
        for start, processingTime in jobs:
            if completedTime < start <= now:
                heapq.heappush(heap,(processingTime, start))
                
        #처리해야할 job하나를 처리함.
        if heap:
            processingTime, start = heapq.heappop(heap)
            #처리시작
            completedTime = now
            now += processingTime  
            #처리완료
            completedCnt += 1
            answer += now - start
        else:
            #아직 처리할 job이 없으면 now 이동
            now += 1
            
    return answer // jobCnt #나머지는 버려