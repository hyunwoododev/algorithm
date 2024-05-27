# https://www.acmicpc.net/problem/1260

import sys
sys.setrecursionlimit(10**6)
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] #정점이 0부터가 아니라 1부터 시작되니깐 N+1로 설정해줘야함 # 🤪틀렸던 부분

# 그래프를 인접 리스트 방식으로 표현하였습니다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

# dfs
dfs_visited = [False] * (N + 1) # 🤪틀렸던 부분
def dfs(v):
    global dfs_visited
    global graph

    dfs_visited[v] = True # 🤪틀렸던 부분
    print(v, end=' ') # 🤪틀렸던 부분

    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)
dfs(V)
print() # 🤪틀렸던 부분

# bfs
bfs_visited = [False] * (N + 1) # 🤪틀렸던 부분
def bfs(v):
    global bfs_visited
    global graph
    queue=deque()
    queue.append(v)
    bfs_visited[v]=True # 🤪틀렸던 부분
    while queue:
        v=queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i]=True # 🤪틀렸던 부분

bfs(V)