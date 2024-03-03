# https://www.acmicpc.net/problem/11404
# 무한을 의미하는 값으로 10억을 설정

INF = int(1e9)

# 노드의 개수 입력 받기
N = int(input())
# 간선의 개수 입력 받기
M = int(input())

# 그래프 초기화: 모든 값에 대해 무한으로 설정
graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    # 자기 자신으로 가는 비용은 0으로 초기화
    graph[i][i] = 0
    
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(M):
    # a에서 b로 가는 비용이 c
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용 중 더 적은 비용으로 갱신
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜 알고리즘 실행
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            # a에서 b로 가는 비용과 a에서 k를 거쳐 b로 가는 비용 중 더 적은 비용으로 갱신
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                
# 결과 출력
for x in range(1, N+1):
    for y in range(1, N+1):
        # 도달할 수 없는 경우, 0을 출력
        if graph[x][y] == INF: print(0, end=' ')
        # 도달할 수 있는 경우, 비용 출력
        else: print(graph[x][y], end=' ')
    print()
