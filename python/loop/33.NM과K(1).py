"""
18290번 문제

크기가 N×M인 격자판의 각 칸에 정수가 하나씩 들어있다. 
이 격자판에서 칸 K개를 선택할 것이고, 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 구하려고 한다. 
단, 선택한 두 칸이 인접하면 안된다. r행 c열에 있는 칸을 (r, c)라고 했을 때, 
(r-1, c), (r+1, c), (r, c-1), (r, c+1)에 있는 칸이 인접한 칸이다.
첫째 줄에 N, M, K가 주어진다. 둘째 줄부터 N개의 줄에 격자판에 들어있는 수가 주어진다.
선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 출력한다.

1 ≤ N, M ≤ 10
1 ≤ K ≤ min(4, N×M)
격자판에 들어있는 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
항상 K개의 칸을 선택할 수 있는 경우만 입력으로 주어진다.
"""
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = -2147483647
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(px, cnt, s):
    global ans
    if cnt == k:
        ans = max(ans, s)
        return

    for x in range(px, n):
        for y in range(m):
            if visited[x][y]:
                continue

            # 인접한 칸에 방문한 칸이 없는지 확인
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                    break
            else:
                # 방문하지 않은 칸이면 탐색
                visited[x][y] = True
                dfs(x, cnt + 1, s + a[x][y])
                visited[x][y] = False


dfs(0, 0, 0)
print(ans)
