"""
1697번 문제

수빈이는 동생과 숨바꼭질을 하고 있다. 
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
"""

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