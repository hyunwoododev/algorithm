from collections import defaultdict, deque

def can_process_request(requests):
    # 도메인별로 요청 시간 인덱스를 저장할 해시맵
    domain_requests = defaultdict(deque)
    results = []
    
    # 각 요청에 대해 순차적으로 처리
    for index, request in enumerate(requests):
        # 오래된 요청을 제거
        while domain_requests[request] and index - domain_requests[request][0] >= 30:
            domain_requests[request].popleft()
        
        # recent_5s 리스트 초기화 및 구성
        recent_5s = []
        for t in domain_requests[request]:
            if index - t < 5:
                recent_5s.append(t)

        # 30초 이내의 요청이 5개 이하이고, 5초 이내의 요청이 2개 이하인 경우 요청 허용
        if len(domain_requests[request]) < 5 and len(recent_5s) < 2:
            domain_requests[request].append(index)  # 현재 요청 인덱스 추가
            results.append("(status: 200, message: ok!)")
        else:
            results.append("(status: 429, message: Too many requests)")
    
    return results

# 예제 입력
requests = ["www.xyz.com", "www.abc.com", "www.xyz.com", "www.pqr.com", 
            "www.abc.com", "www.xyz.com", "www.xyz.com", "www.abc.com", "www.xyz.com"]

# 함수 실행 및 결과 출력
result = can_process_request(requests)
print(result)
