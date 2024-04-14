# https://leetcode.com/problems/course-schedule/

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            current = q.popleft()
            for i in graph[current]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        return sum(indegree) == 0
