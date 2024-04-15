# https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()        
        posDiag = set()  
        negDiag = set() 

        res = []
        board = [["."] * n for i in range(n)] 

        def backtrack(r):
            if r == n: 
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
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