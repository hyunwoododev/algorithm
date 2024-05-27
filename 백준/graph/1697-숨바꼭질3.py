# https://www.acmicpc.net/problem/13549
from collections import deque

MAX = 200000

def bfs(start, goal):
   check = [False] * MAX
   dist = [-1] * MAX #이게 킥이네

   q = deque()
   q.append(start)
   check[start] = True
   dist[start] = 0

   while q:
       now = q.popleft()

       # 순간이동
       if now * 2 < MAX and not check[now * 2]:
           q.append(now * 2)
           check[now * 2] = True
           dist[now * 2] = dist[now]

       # 걷기
       for next_pos in (now - 1, now + 1):
           if 0 <= next_pos < MAX and not check[next_pos]:
               q.append(next_pos)
               check[next_pos] = True
               dist[next_pos] = dist[now] + 1

   return dist[goal]

n, m = map(int, input().split())
print(bfs(n, m))