# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def getParent(parent,node):
    if parent[node] == node: return node
    return getParent(parent, parent[node])
    
def unionParent(parent, node1, node2):
    parent1 = getParent(parent, node1)
    parent2 = getParent(parent, node2)
    
    if parent1 < parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2

    
def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    
    if (a==b):
        return True
    else:
        return False
    
def solution(n, costs):
    parent = [0] * (n)
    for i in range(n):
        parent[i] = i
    total_cost = 0
    #costs에는 a, b, cost가 들어있음
    costs.sort(key = lambda x : x[2])
    #크루스칼
    for a, b, cost in costs:
        if findParent(parent, a, b) == False :
            unionParent(parent, a, b)
            total_cost += cost
        
    return total_cost