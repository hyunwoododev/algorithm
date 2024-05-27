#  https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=true

class UnionFind:
    def __init__(self, n):
        # `n`개의 요소로 초기화된 Union-Find 자료 구조를 초기화합니다.
        self.parent = list(range(n))  # 초기에는 각 노드가 자신의 부모입니다.
        self.rank = [1] * n  # 트리를 평평하게 유지하기 위해 랭크를 사용합니다.
        self.size = [1] * n  # 각 구성 요소의 크기를 추적하기 위한 크기 배열입니다.

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # `u`와 `v`를 포함하는 집합을 랭크에 따라 합칩니다.
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.parent[root_v] = root_u
                self.size[root_u] += self.size[root_v]
                self.rank[root_u] += 1

    def get_size(self, u):
        # 노드 `u`가 속한 집합의 크기를 반환합니다.
        return self.size[self.find(u)]

def journeyToMoon(n, astronaut):
    uf = UnionFind(n)
    
    # 각 우주비행사 쌍에 대해 유니온 연산을 수행합니다.
    for u, v in astronaut:
        uf.union(u, v)
    
    # 각 국가의 크기를 추적합니다.
    country_sizes = []
    for i in range(n):
        if uf.find(i) == i:
            country_sizes.append(uf.get_size(i))
    
    # 가능한 모든 페어의 수를 계산합니다.
    total_pairs = n * (n - 1) // 2
    # 같은 국가에 속한 페어의 수를 계산합니다.
    same_country_pairs = sum(size * (size - 1) // 2 for size in country_sizes)
    
    # 다른 국가에 속한 페어의 수를 반환합니다.
    return total_pairs - same_country_pairs
