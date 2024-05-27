# https://www.acmicpc.net/problem/11724

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
visited = [False] * (N+1)

# 그래프를 인접 행렬 방식으로 표현하였습니다.
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1 # 🤪틀렸던 부분

def dfs(n):
    for i in range(len(graph[n])): # 🤪틀렸던 부분
        if graph[n][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i)

# dfs init
res = 0
for i in range(1,N+1):# 🤪틀렸던 부분
    if not visited[i]:
        dfs(i)
        res += 1

print(res)