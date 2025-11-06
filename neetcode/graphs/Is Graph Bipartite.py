# https://leetcode.com/problems/is-graph-bipartite/

from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        for i in range(len(graph)):
            if colors[i] != 0:
                continue
            
            queue = deque()
            queue.append(i)
            colors[i] = 1
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        # 인접한 정점이 색칠되지 않았다면, 현재 정점과 다른 색으로 색칠
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        # 인접한 정점이 같은 색이라면, 이분 그래프가 아님
                        return False
        return True
                 