"""
13549번 문제

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

0 무한루프 개조심하자.!!!!!!!!!!
"""
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