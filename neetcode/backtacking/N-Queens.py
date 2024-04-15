# https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()        # 각 열에 퀸이 위치하는지를 나타내는 집합
        posDiag = set()   # 양 대각선 방향에 퀸이 위치하는지를 나타내는 집합 (r + c)
        negDiag = set()   # 음 대각선 방향에 퀸이 위치하는지를 나타내는 집합 (r - c)

        res = []          # 결과를 저장할 리스트
        board = [["."] * n for i in range(n)]  # 체스판을 나타내는 이차원 리스트

        # 백트래킹을 통해 가능한 퀸의 배치를 찾는 함수
        def backtrack(r):
            if r == n:  # 퀸을 모두 배치했을 때 결과를 저장하고 종료
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # 현재 열, 양 대각선, 음 대각선 상에 퀸이 위치하는지 확인
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # 퀸을 배치하고 해당 위치에 대한 집합을 업데이트
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # 다음 행에 대해 재귀적으로 호출
                backtrack(r + 1)

                # 백트래킹을 위해 퀸을 제거하고 해당 위치에 대한 집합을 업데이트
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

                board[r][c] = "."

        backtrack(0)  # 백트래킹 시작
        return res    # 모든 가능한 배치 결과 반환