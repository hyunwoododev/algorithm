# https://www.acmicpc.net/problem/15657

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []

def dfs(prev):
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(len(arr)):
        if len(s) == 0 or arr[i] >= arr[prev]:
            s.append(arr[i])
            dfs(i)
            s.pop()

dfs(0)
