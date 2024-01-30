"""
1260번 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
"""
import sys
sys.setrecursionlimit(10**6)
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)] #정점이 0부터가 아니라 1부터 시작되니깐 N+1로 설정해줘야함

# 그래프를 인접 리스트 방식으로 표현하였습니다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

# dfs
dfs_visited = [False] * (N + 1)
def dfs(v):
    global dfs_visited
    global graph

    dfs_visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)
dfs(V)
print()

# bfs
bfs_visited = [False] * (N + 1)
def bfs(v):
    global bfs_visited
    global graph
    queue=deque()
    queue.append(v)
    bfs_visited[v]=True
    while queue: # queue가 비어있지 않다면
        v=queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_visited[i]=True

bfs(V)