# https://www.acmicpc.net/problem/1707
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())
def DFS(start, visited, graph, group):
    visited[start] = group  # 현재 노드의 그룹 저장
    # 인접 노드 탐색
    for v in graph[start]:
        if visited[v] == 0:  # 아직 방문하지 않은 노드
            # -group : 현재 노드의 그룹과 다른 값 전달
            result = DFS(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:  # 이미 방문한 곳 중에서 노드가 현재 그룹과 같으면 이분 그래프가 아님
                return False
    return True

for _ in range(k):
    # graph 생성
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    
    # 그래프를 인접 리스트 방식으로 표현하였습니다.
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if visited[i] == 0:
            result = (DFS(i, visited, graph, 1))
            if not result: # 이게 정말 중요한 부분이다. for문을 돌면서 하나라도 False가 나오면 바로 NO를 출력해야한다.
                break
            
    print("YES") if result else print("NO")

        
    
        
    