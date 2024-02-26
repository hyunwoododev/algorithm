# https://www.acmicpc.net/problem/15649
# [1,3] 과 [3, 1]이어도 될때.
N,M = map(int,input().split())
stack = []
def dfs():
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
        
    for i in range(1,N+1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()
dfs()