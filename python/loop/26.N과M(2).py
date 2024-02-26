# https://www.acmicpc.net/problem/15650

N,M = map(int,input().split())
stack =[]
def dfs(idx):
    if len(stack) == M:
        print(' '.join(map(str,stack)))
        return
    
    for i in range(idx,N+1):
        if i not in stack:
            stack.append(i)
            dfs(i+1) # 여기 idx+1 아님 😣😣😣😣
            stack.pop(i)
dfs(1)