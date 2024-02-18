from collections import deque

dx = [0, 0, -1, 1]  # x축 이동 방향 (상, 하)
dy = [-1, 1, 0, 0]  # y축 이동 방향 (좌, 우)

# 게임 보드 또는 테이블에서 빈 공간 또는 블록을 찾는 함수
def find_block(board, f):
    empty_board_list = []  # 찾은 블록 또는 빈 공간의 좌표 리스트
    visited = [[False] * len(board[0]) for _ in range(len(board))]  # 방문 여부 체크

    for i in range(len(board)):
        for j in range(len(board[i])):
            if not visited[i][j] and board[i][j] == f:
                queue = deque([(i, j)])
                board[i][j] = f ^ 1  # 블록을 찾으면 상태 반전 (빈 공간 ↔ 블록)
                visited[i][j] = True
                lst = [(i, j)]  # 현재 블록 또는 빈 공간의 좌표

                while queue:
                    x, y = queue.popleft()
                    for _ in range(4):  # 상하좌우 탐색
                        nx, ny = x + dx[_], y + dy[_]
                        if nx < 0 or nx > len(board) - 1 or ny < 0 or ny > len(board) - 1:
                            continue
                        elif board[nx][ny] == f:
                            queue.append((nx, ny))
                            board[nx][ny] = f ^ 1  # 상태 반전
                            visited[nx][ny] = True
                            lst.append((nx, ny))
                empty_board_list.append(lst)  # 찾은 블록 또는 빈 공간 추가

    return empty_board_list

# 블록의 좌표를 기반으로 2D 테이블 생성
def make_table(block):
    x, y = zip(*block)
    c, r = max(x) - min(x) + 1, max(y) - min(y) + 1
    table = [[0] * r for _ in range(c)]

    for i, j in block:
        i, j = i - min(x), j - min(y)
        table[i][j] = 1
    return table

# 퍼즐 조각을 오른쪽으로 90도 회전
def rotate(puzzle):
    rotate = [[0] * len(puzzle) for _ in range(len(puzzle[0]))]
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 1:
                count += 1
            rotate[j][len(puzzle) - 1 - i] = puzzle[i][j]
    return rotate, count

# 메인 솔루션 함수
def solution(game_board, table):
    answer = 0
    empty_blocks = find_block(game_board, 0)  # 게임 보드에서 빈 공간 찾기
    puzzles = find_block(table, 1)  # 테이블에서 퍼즐 조각 찾기

    for empty in empty_blocks:  # 모든 빈 공간에 대해
        filled = False
        table = make_table(empty)  # 빈 공간의 2D 테이블 생성

        for puzzle_origin in puzzles:  # 모든 퍼즐 조각에 대해
            if filled == True:
                break

            puzzle = make_table(puzzle_origin)  # 퍼즐 조각의 2D 테이블 생성
            for i in range(4):  # 4번 회전
                puzzle, count = rotate(puzzle)

                if table == puzzle:  # 퍼즐 조각이 빈 공간에 맞으면
                    answer += count  # 맞춘 퍼즐 조각 수 증가
                    puzzles.remove(puzzle_origin)  # 사용한 퍼즐 조각 제거
                    filled = True
                    break

    return answer
