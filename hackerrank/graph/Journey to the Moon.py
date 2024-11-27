#  https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=true

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 초기에는 각 노드가 자신의 부모입니다.
        self.rank = [1] * n  # 트리를 평평하게 유지하기 위해 랭크를 사용합니다.

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
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def journeyToMoon(n, astronaut):
    uf = UnionFind(n)
    # 각 집합의 크기를 추적할 리스트를 초기화합니다.
    size = [1] * n

    # 각 우주비행사 쌍에 대해 유니온 연산을 수행합니다.
    for u, v in astronaut:
        root_u = uf.find(u)
        root_v = uf.find(v)
        if root_u != root_v:
            # 두 집합을 합치고, 합친 집합의 크기를 업데이트합니다.
            if uf.union(u, v):
                new_root = uf.find(u)
                if new_root == root_u:
                    size[root_u] += size[root_v]
                    size[root_v] = 0
                else:
                    size[root_v] += size[root_u]
                    size[root_u] = 0
    
    # 각 국가의 크기를 추적합니다.
    country_sizes = [size[i] for i in range(n) if uf.find(i) == i]
    
    # 가능한 모든 페어의 수를 계산합니다.
    total_pairs = n * (n - 1) // 2
    # 같은 국가에 속한 페어의 수를 계산합니다.
    same_country_pairs = sum(size * (size - 1) // 2 for size in country_sizes)
    

    print(total_pairs, same_country_pairs)
    # 다른 국가에 속한 페어의 수를 반환합니다.
    return total_pairs - same_country_pairs
