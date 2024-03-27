# 문제 :
# N×N 크기의 보드가 있습니다. 보드의 각 칸에는 사탕이 놓여져 있고, 사탕의 색은 모두 같지 않습니다. 사탕의 색은 모두 같지 않습니다.
# 이제 다음과 같은 연산을 수행할 수 있습니다.

# 인접한 두 칸을 골라 사탕을 서로 교환합니다. (교환하려는 두 칸은 가로로 이웃하거나 세로로 이웃해야 합니다.)
# 모든 인접한 두 칸에 대해 연산을 수행한 후에, 보드의 모든 행 또는 모든 열에 포함된 같은 색상의 사탕의 최대 연속하는 개수를 구합니다.
# 보드의 크기 N과 보드에 놓인 사탕의 정보가 주어질 때, 연산을 한 번 수행하고 나서 얻을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하세요.


# 풀이
N = int(input()) # 보드의 크기 입력
board = [list(input()) for _ in range(N)] #[['C', 'C', 'P'], ['C', 'C', 'P'], ['P', 'P', 'C']]

def check(board):
    ans = 0
    for i in range(N):
        cnt = 1
        for j in range(1, N): # 가로로 연속되는 사탕 체크
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        
        cnt = 1
        for j in range(1, N): # 세로로 연속되는 사탕 체크
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

    return ans

ans = 0

for i in range(N):
    for j in range(N):
        if j+1 < N: # 인접한 사탕끼리 교환 (가로)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, check(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
        if i+1 < N: # 인접한 사탕끼리 교환 (세로)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, check(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)


