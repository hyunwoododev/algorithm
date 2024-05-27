# https://www.acmicpc.net/problem/2178
from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

def bfs(N, M, graph):
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = set()
    q = deque()
    visited.add((0, 0))  # 시작점을 (0, 0)으로 설정
    q.append((0, 0, 1)) #  칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.라고 문제에 명시되어 있음 

    while q:
        row, col, dis = q.popleft()
        if row == N - 1 and col == M - 1:
            print(dis)
            return  # 목표 지점에 도달하면 거리 출력 후 함수 종료
        
        for dr, dc in directions:
            tr = row + dr
            tc = col + dc
            if (
                tr >= 0
                and tr < N
                and tc >= 0
                and tc < M
                and (tr, tc) not in visited
                and graph[tr][tc] == 1  # 이동 가능한 칸인지 확인
            ):
                visited.add((tr, tc))
                q.append((tr, tc, dis + 1))
    
    print(-1) 

bfs(N, M, graph)
