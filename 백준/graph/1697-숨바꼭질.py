# https://www.acmicpc.net/problem/1697

import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
visited = [0 for _ in range(100001)] # 100001을 조심해야함. 100000아님.

def bfs(cnt):
    queue = deque()
    queue.append(cnt)
    while queue:
        c = queue.popleft()
        if c == K:
            return visited[c]
        for i in (c-1, c+1, c*2):
            if 0 <= i <= 100000 and not visited[i]: # 🤪틀렸던 부분, 조건을 정말정말 잘 체크하자 제발좀..
                queue.append(i)
                visited[i] = visited[c]+1

print(bfs(N))

from collections import deque

def bfs(N, K):
    if N == K:
        return 0
    
    visited = set()
    q = deque()
    q.append(N)
    visited.add(N)
    time = 0

    while q:
        for _ in range(len(q)):  # 현재 레벨의 모든 노드를 처리
            current = q.popleft()
            if current == K:
                return time
            for next_pos in (current + 1, current - 1, 2 * current):
                if 0 <= next_pos <= 100000 and next_pos not in visited:
                    visited.add(next_pos)
                    q.append(next_pos)
        time += 1
    return -1

N, K = map(int, input().split())
print(bfs(N, K))
