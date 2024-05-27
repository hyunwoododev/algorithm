# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# graph 생성
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))
    
def bfs(r,c):
    visited = set()
    q = deque()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    visited.add((r,c))
    q.append((r,c))
    graph[r][c] = 0
    count = 0
    while q:
        row, col = q.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == 1 and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append((nr,nc))
                graph[nr][nc] = 0
                count += 1
    return count + 1
cnt = []
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            cnt.append(bfs(r,c))
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])