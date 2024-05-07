"""
https://school.programmers.co.kr/learn/courses/30/lessons/42627
"""
import heapq

def solution(jobs):
    answer = 0
    completeTask = 0
    now = 0
    start = -1
    copyJob = jobs[:]
    heap = []
    
    while len(copyJob) > completeTask:
        # 지금 처리할 수 있는 job 가져오기 + 처리시간이 짧은순으로 우선순위  
        # 여기서 추가된 모든 작업들은 아래에서 다 처리된다. 자주쓸것같으니 체크.       
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,[job[1],job[0]])
        # 처리할 job이 있다면, 첫번째 job을 처리
        if len(heap) > 0:
            jobToProcess = heapq.heappop(heap)
            start = now # start는 가장 마지막에 처리된 job의 시작시간
            # 처리한 시간만큼 now 증가
            now += jobToProcess[0]
            # 처리하는데 걸린 시간 추가(대기시간 부터)
            answer += now - jobToProcess[1]
            completeTask += 1

        # 처리할 job이 없다면, 처리할 job이 있을때까지 1씩 증가
        else:
            now += 1
            
    return answer // len(jobs)