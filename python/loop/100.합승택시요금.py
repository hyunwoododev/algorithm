# https://school.programmers.co.kr/learn/courses/30/lessons/49191

def solution(n, s, a, b, fares):
    # 무한대 값을 나타내는 변수 설정
    INF = int(1e9)
    
    # 최종 답을 저장할 변수, 초기값을 무한대로 설정하여 최소값을 찾을 수 있게 함
    ans = INF
    
    # 그래프 초기화: n+1 크기의 2차원 리스트를 생성하고 모든 값을 INF로 설정
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    # 자기 자신으로의 경로 비용을 0으로 초기화
    for i in range(n+1):
        graph[i][i] = 0
        
    # 주어진 요금 정보를 바탕으로 그래프의 간선 비용 설정
    # 양방향 그래프이므로, i에서 j로 가는 비용과 j에서 i로 가는 비용이 동일
    for i, j, c in fares:
        graph[i][j] = c
        graph[j][i] = c
    
    # 플로이드-워셜 알고리즘 적용: 모든 노드 쌍에 대해 최단 경로 계산
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                # i에서 j로 가는 비용과 i에서 k를 거쳐 j로 가는 비용 중 더 작은 값으로 갱신
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # s에서 출발하여 a와 b까지 각각 가는 경우 중, 
    # 어떤 노드 i에서 합승을 종료하고 각자 목적지로 가는 비용이 최소가 되는 경우를 찾음
    for i in range(1, n+1):
        # s에서 i까지, 그리고 i에서 a와 b까지 가는 최단 경로의 합을 계산하여
        # 이전에 계산된 최소값(ans)와 비교하여 더 작은 값을 ans에 저장
        ans = min(graph[s][i] + graph[i][a] + graph[i][b], ans)
        
    # 최종적으로 계산된 최소 비용을 반환
    return ans
