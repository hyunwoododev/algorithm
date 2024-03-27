# https://leetcode.com/problems/word-search/description/

from collections import defaultdict, Counter

class Solution:
    # 주어진 보드에서 단어가 존재하는지 수평 또는 수직으로 탐색하여 확인하는 함수.
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 보드의 행과 열의 크기를 구함
        ROWS, COLS = len(board), len(board[0])
        
        # 방문한 위치를 추적하기 위한 집합
        path = set()

        # 단어의 존재 여부를 확인하기 위한 깊이 우선 탐색(DFS) 함수
        def dfs(r, c, i):
            # 기본 사례: 전체 단어를 찾은 경우
            if i == len(word):
                return True
            
            # 범위를 벗어나거나 문자가 일치하지 않거나 위치가 이미 방문한 경우 False 반환
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            
            # 현재 셀을 방문한 것으로 표시
            path.add((r, c))

            # 네 방향으로 재귀적으로 탐색
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # 백트래킹을 위해 현재 셀을 방문한 집합에서 제거
            path.remove((r, c))
            return res

        # 보드 내 각 문자의 빈도를 계산
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        # 단어의 첫 글자보다 마지막 글자의 빈도가 더 낮은 경우, 효율성을 위해 검색 방향을 반대로 함
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
            
        # 각 셀에서 DFS 시작
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
