import heapq

def solution(jobs):
    # 작업 요청부터 종료까지 걸린 시간 answer
    # 현재 시간 now
    # 처리한 일의 갯수 i
    answer, now, i = 0, 0, 0
    
    
    start = -1	#이전 작업 시작 완료 시간
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            #요청 시간이 이전작업의 시작시간 보다 크고, 현재 시간보다 작거나 같은 작업을 최소 힙에 삽입
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])	#작업 걸리는 시간, 시작 시간으로 추가
        
        if len(heap) > 0:   #처리할 작업이 있는 경우 
            cur = heapq.heappop(heap)
            start = now		#시작 시간 현재 시간으로 갱신
            now += cur[0]	#현재 시간에서 작업 소요 시간을 더해 현재 시간 갱신
            answer += now - cur[1] #대기 시간 및 처리 시간 누적
            i += 1 #일 하나 처리했으므로 +1
            
        else:   #처리할 작업이 없는 경우 현재 시간 1 증가
            now += 1
    return answer // len(jobs)