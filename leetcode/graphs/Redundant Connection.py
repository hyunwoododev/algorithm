# https://leetcode.com/problems/redundant-connection/description/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def getParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.getParent(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.getParent(node1)
        parent2 = self.getParent(node2)
        
        if parent1 != parent2:
            if self.rank[parent1] > self.rank[parent2]:
                self.parent[parent2] = parent1
            elif self.rank[parent1] < self.rank[parent2]:
                self.parent[parent1] = parent2
            else:
                self.parent[parent2] = parent1
                self.rank[parent1] += 1

    def find(self, node1, node2):
        return self.getParent(node1) == self.getParent(node2)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        for a, b in edges:
            if uf.find(a, b):
                return [a, b]
            else:
                uf.union(a, b)
