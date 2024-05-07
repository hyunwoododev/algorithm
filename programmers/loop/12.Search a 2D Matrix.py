#  https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 행렬의 행과 열의 수를 구합니다.
        ROWS, COLS = len(matrix), len(matrix[0])

        # 이진 검색을 위한 상단(top)과 하단(bot) 포인터를 초기화합니다.
        top, bot = 0, ROWS - 1
        while top <= bot:
            # 중앙값을 기준으로 행을 찾습니다.
            row = (top + bot) // 2
            # 대상 값이 현재 행의 마지막 요소보다 크면, 상단 포인터를 조정합니다.
            if target > matrix[row][-1]:
                top = row + 1
            # 대상 값이 현재 행의 첫 번째 요소보다 작으면, 하단 포인터를 조정합니다.
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                # 대상 값이 현재 행 범위 내에 있으면 반복을 중단합니다.
                break

        # 대상 값이 어떤 행 범위에도 속하지 않으면 False를 반환합니다.
        if not (top <= bot):
            return False
        
        # 대상 값이 속하는 행을 찾습니다.
        row = (top + bot) // 2
        # 해당 행 내에서 대상 값을 찾기 위해 좌우 포인터를 초기화합니다.
        l, r = 0, COLS - 1
        while l <= r:
            # 중앙값을 기준으로 열에서 위치를 찾습니다.
            m = (l + r) // 2
            # 대상 값이 중앙값보다 크면, 왼쪽 포인터를 조정합니다.
            if target > matrix[row][m]:
                l = m + 1
            # 대상 값이 중앙값보다 작으면, 오른쪽 포인터를 조정합니다.
            elif target < matrix[row][m]:
                r = m - 1
            else:
                # 대상 값이 중앙값과 일치하면 True를 반환합니다.
                return True
        # 대상 값이 해당 행에 없으면 False를 반환합니다.
        return False

