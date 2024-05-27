# https://www.acmicpc.net/problem/7562

import sys
from collections import deque
sys.setrecursionlimit(10**6) # 🤪틀렸던 부분, 왜계속 빼먹니?
K = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1 , 1, -2, 2, -2, 2, -1, 1]


def bfs(start, graph, N, end):
    startX, startY = start[0], start[1]
    endX, endY = end[0], end[1]
    graph[startX][startY] = 1
    q = deque()
    q.append((startX, startY))

    while q:
        a,b = q.popleft()
        for ix in range(8):
            nx = a + dx[ix]
            ny = b + dy[ix]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b] + 1
                q.append((nx,ny))

    return graph[endX][endY] - 1 # 🤪틀렸던 부분, 이거 왜 1빼야해

for _ in range(K):
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    start= list(map(int, input().split()))
    end = list(map(int,input().split()))
    res = bfs(start, graph, N , end)
    print(res)

