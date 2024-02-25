# https://www.acmicpc.net/problem/15591

import sys
from collections import deque
input = sys.stdin.readline

# N: 동영상의 수, Q: 쿼리의 수
N, Q = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 그래프 구성
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

# BFS 함수 정의
def bfs(v, k):
    visited = [False] * (N + 1)
    visited[v] = True
    queue = deque([v])
    count = 0
    
    while queue:
        current = queue.popleft()
        print(current)
        for next, usado in graph[current]:
            if not visited[next] and usado >= k:
                visited[next] = True
                queue.append(next)
                count += 1
    return count

# 쿼리 처리
for _ in range(Q):
    k, v = map(int, input().split())
    print(bfs(v, k))
