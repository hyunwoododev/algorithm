"""
14889번 문제

오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 
축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 
팀에 더해지는 능력치는 Sij와 Sji이다.
... (이하 생략)
"""

import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 2147000000
res = INF

def DFS(cnt,idx):
    global res
    if cnt == N//2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B +=board[i][j]
        res = min(res, abs(A-B))
        return
    for i in range(idx,N):
        if not visited[i]: #반드시 필요하지는 않음
            visited[i] = True
            DFS(cnt+1,i+1)
            visited[i] = False
            
DFS(0,0)
print(res)