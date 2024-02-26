# """
# https://www.acmicpc.net/problem/13549
# """
from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001  # 각 위치까지 도달하는 데 걸린 시간을 저장. 방문하지 않은 위치는 -1로 초기화

def bfs():
    q = deque([N])
    visited[N] = 0  # 시작 위치의 시간을 0으로 설정

    while q:
        v = q.popleft()
        if v == K:  # 목표 위치에 도달한 경우
            return visited[v]

        # 순간이동
        if 2*v < 100001 and visited[2*v] == -1:
            visited[2*v] = visited[v]  # 순간이동 시간 추가 없음
            q.appendleft(2*v)  # 순간이동한 위치를 큐의 앞쪽에 추가하여 우선적으로 처리

        # 걷기: -1, +1
        for next_v in (v-1, v+1):
            if 0 <= next_v < 100001 and visited[next_v] == -1:
                visited[next_v] = visited[v] + 1  # 걷는 경우 시간 1초 추가
                q.append(next_v)

    return visited[K]

print(bfs())
