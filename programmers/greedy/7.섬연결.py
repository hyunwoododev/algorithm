# https://school.programmers.co.kr/learn/courses/30/lessons/42861
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
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
            rank1 = self.rank[parent1]
            rank2 = self.rank[parent2]
            
            if rank1 > rank2:
                self.parent[parent2] = parent1
            elif rank1 < rank2:
                self.parent[parent1] = parent2
            else:
                self.parent[parent2] = parent1
                self.rank[parent1] += 1

    def check(self, node1, node2):
        return self.getParent(node1) == self.getParent(node2)

def solution(n, costs):
    uf = UnionFind(n)
    costs.sort(key=lambda x: x[2])
    total = 0
    
    for a, b, cost in costs:
        if not uf.check(a, b):
            uf.union(a, b)
            total += cost
    
    return total
