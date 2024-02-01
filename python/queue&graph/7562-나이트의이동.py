# """
# 7562번 문제

# https://www.acmicpc.net/problem/7562

# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
# 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 세 줄로 이루어져 있다. 
# 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
# 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
# """
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

