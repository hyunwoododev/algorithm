# https://leetcode.com/problems/course-schedule-ii/description/
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        indegree = [0] * numCourses
        graph = [[] for i in range(numCourses)]
        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        while q:
            course = q.popleft()
            output.append(course)
            for i in graph[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        return output if len(output) == numCourses else []