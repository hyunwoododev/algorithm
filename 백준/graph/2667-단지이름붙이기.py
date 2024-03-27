"""
2667번 문제

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""
import sys
from collections import deque
sys.setrecursionlimit(10**6) # 🤪틀렸던 부분,
input = sys.stdin.readline

# 인접 좌표 구성
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# graph 생성
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().rstrip())))# 🤪틀렸던 부분, 진짜 중요! 개행조심

def bfs(a, b):
    global graph
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])