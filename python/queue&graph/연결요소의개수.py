"""
11724번 문제

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
visited = [False] * (N+1)

# graph 생성
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

def dfs(n):
    for i in range(len(graph[n])):
        if graph[n][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i)

# dfs init
res = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        res += 1

print(res)