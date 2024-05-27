"""
https://school.programmers.co.kr/learn/courses/30/lessons/49189
"""
from collections import deque
def solution(n, edge):
    graph = [[] for i in range(len(edge)+1)]
    for n1,n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    visited = [-1] * len(edge)
    def bfs():
        q = deque()
        q.append(1)
        visited[1] = 0
        while q:
            idx = q.popleft()
            for i in graph[idx]:
                if visited[i] == -1:
                    q.append(i)
                    visited[i] = visited[idx] + 1
    bfs()
    maxValue = max(visited)
    return visited.count(maxValue)