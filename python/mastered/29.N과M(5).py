# https://www.acmicpc.net/problem/15654

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s= []
def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    for i in range(len(arr)):
        if not arr[i] in s:
            s.append(arr[i])
            dfs()
            s.pop()

dfs()



