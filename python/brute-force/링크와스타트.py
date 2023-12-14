"""
15661번

오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 
축구는 평일 오후에 하고 의무 참석도 아니다. 
축구를 하기 위해 모인 사람은 총 N명이다. 이제 스타트 팀과 링크 팀으로 사람들을 나눠야 한다. 
두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.
... (이하 생략)
"""

import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 2147000000
res = INF

def DFS(cnt):
    global res
    if cnt == N:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B += board[i][j]
        res = min(res, abs(A-B))
        return

    #i번째를 뽑는 경우
    visited[cnt] = True
    DFS(cnt+1)
    visited[cnt] = False
    # i번째를 안뽑는 경우
    DFS(cnt+1)

DFS(0)
print(res)
