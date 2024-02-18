# https://school.programmers.co.kr/learn/courses/30/lessons/42861
def getParent(parent, x):
    if parent[x] == x: return x
    return getParent(parent, parent[x])
    
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b
    
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