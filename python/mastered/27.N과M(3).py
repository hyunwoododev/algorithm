# https://www.acmicpc.net/problem/15651
N,M = map(int,input().split())
stack = []
def dfs():
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    
    for i in range(1,N+1):
        stack.append(i)
        dfs()
        stack.pop()
dfs()