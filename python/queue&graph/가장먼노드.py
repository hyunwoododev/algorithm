"""
https://school.programmers.co.kr/learn/courses/30/lessons/49189
"""
from collections import deque

def solution(n, edge):
    graph =[[0] for _ in range(n+1)]
    visited = [False]*(n+1)

    for i in edge:
        a,b = i
        graph[a].append(b)
        graph[b].append(a)

    def bfs():
        q = deque()
        q.append(graph[1])
        visited[1] = True
        while q:
            arr = q.popleft()
            count = arr[0]
            for i in arr[1:]:
                if not visited[i]:
                    visited[i] = True
                    graph[i][0] = count+1
                    q.append(graph[i])
    bfs()
    newArr = list(map(lambda x:x[0], graph))
    maxNum = max(newArr)
    return newArr.count(maxNum)