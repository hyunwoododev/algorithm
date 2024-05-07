"""
https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""
import heapq

def solution(jobs):
    answer = 0  # 모든 작업을 완료하는데 걸린 총 시간
    now = 0  # 현재 시간
    completedJob = 0  # 완료된 작업 수
    jobCnt = len(jobs)  # 전체 작업 수
    
    jobHeap = []  # 작업을 시작 시간 기준으로 정렬하기 위한 힙
    for s, p in jobs:
        # 작업을 (시작 시간, 처리 시간)의 튜플로 jobHeap에 추가
        heapq.heappush(jobHeap, (s, p))
    
    tmpHeap = []  # 현재 시간에서 처리할 수 있는 작업들을 처리 시간 기준으로 정렬하기 위한 힙
    
    while completedJob < jobCnt:  # 모든 작업이 완료될 때까지 반복
        # 현재 시간 이하에서 시작 가능한 모든 작업을 tmpHeap으로 옮김
        while jobHeap and jobHeap[0][0] <= now:
            start, processingTime = heapq.heappop(jobHeap)
            # 처리 시간을 기준으로 tmpHeap에 작업 추가
            heapq.heappush(tmpHeap, (processingTime, start))
        
        if tmpHeap:
            # 처리 시간이 가장 짧은 작업을 tmpHeap에서 꺼냄
            processingTime, start = heapq.heappop(tmpHeap)
            now += processingTime  # 현재 시간 업데이트
            answer += now - start  # 대기 시간 포함하여 총 시간에 추가
            completedJob += 1  # 완료된 작업 수 업데이트
        else:
            # 처리할 작업이 없으면 현재 시간을 1 증가
            now += 1
    
    # 모든 작업을 완료하는데 걸린 총 시간의 평균 반환
    return answer // jobCnt
