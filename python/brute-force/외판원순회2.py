"""
10971번 문제
1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다. (길이 없을 수도 있다) 
이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다. 
단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 
이런 여행 경로는 여러 가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.
각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. 
W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 비용은 대칭적이지 않다. 
즉, W[i][j] 는 W[j][i]와 다를 수 있다.
모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 
경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.
N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.

첫째 줄에 도시의 수 N이 주어진다. (2 ≤ N ≤ 10) 다음 N개의 줄에는 비용 행렬이 주어진다. 
각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다. 
W[i][j]는 도시 i에서 j로 가기 위한 비용을 나타낸다.
항상 순회할 수 있는 경우만 입력으로 주어진다.
"""


import sys
# 처음 번호, 현재 번호, 합, 갯수를 넘겨주었다.
# 만약 갯수가 N과 같다면 제일 마지막 도시이기 때문에 처음 도시로 가는 비용을 추가하고 작은지 큰지 비교한다.
def dfs(start, now, value, cnt):
    global ans # global 키워드는 함수 내에서 전역 변수의 값을 변경할 때 사용합니다. 
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0


N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [0] * N
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)