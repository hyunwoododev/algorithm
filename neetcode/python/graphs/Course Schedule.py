# https://leetcode.com/problems/course-schedule/

from collections import deque


# bfs
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


# dfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False

            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)

            preMap[crs] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
