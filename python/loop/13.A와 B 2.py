# https://www.acmicpc.net/problem/12919

import sys
S=list(input())
T=list(input())
def dfs(t): # 문자열 T 리스트를 입력받아
    if t==S: # 리스트끼리 같음이 표시가되네?
        print(1)
        sys.exit()
    # 문자열 S로 변환할 수 없는 경우  
    if len(t)==0:
        return 
    if t[-1]=='A': # 마지막이 A이면 
        dfs(t[:-1]) # 제거해서 재귀
    if t[0]=='B': # 처음이 B이면
        dfs(t[1:][::-1]) # B제거하고, 뒤집어서 재귀
dfs(T)
print(0)

