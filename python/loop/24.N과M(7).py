# https://www.acmicpc.net/submit/15656
# import sys
# input = sys.stdin.readline

# N,M = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
# s =[]

# def dfs():
#     if len(s) == M:
#         print(' '.join(map(str,s)))
#         return 
#     for i in range(len(arr)):
#         s.append(arr[i])
#         dfs()
#         s.pop()
# dfs()


N, M = map(int,input().split())
arr = list(map(int, input().split()))

arr.sort()

stack = []
def dfs():
    if len(stack) == M:
        print(" ".join(map(str,stack)))
        return
    
    for i in range(len(arr)):
        stack.append(arr[i])
        dfs()
        stack.pop()

dfs()