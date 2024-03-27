"""
11724번 문제

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
(1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

현우 해석 :
-> 간선이 주어진 경우에 해당.
-> 몇개의 집합으로 이루어져 있는지를 구하는 문제.
-> 시작점이 정해지지 않은 경우에 해당 = for문으로 모든 정점을 시작점으로 설정해줘야함.
-> 정점번호의 시작이 0이 아닌 1부터 시작하는 경우에 해당.😣😣😣😣
"""
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