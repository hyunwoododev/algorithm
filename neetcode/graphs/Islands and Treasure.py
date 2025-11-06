# https://neetcode.io/problems/islands-and-treasure

from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]):
        ROWS, COLS = len(grid), len(grid[0])  # 격자의 행과 열의 크기를 구합니다.
        visit = set()  # 방문한 위치를 저장할 집합입니다.
        q = deque()  # BFS 탐색을 위한 큐입니다.
        inf = 2147483647  # INF 값을 2^31 - 1로 정의

        def addRooms(r, c):
            # 유효하지 않은 위치를 확인합니다 (범위를 벗어나거나 이미 방문했거나 물인 경우)
            if (
                r < 0
                or c < 0  # 범위를 벗어난 경우
                or r >= ROWS
                or c >= COLS  # 범위를 벗어난 경우
                or (r, c) in visit  # 이미 방문한 경우
                or grid[r][c] == -1  # 물인 경우
            ):
                return
            visit.add((r, c))  # 방문한 위치를 집합에 추가합니다.
            q.append([r, c])  # 큐에 추가합니다.

        # 모든 보물 상자(0)의 위치를 큐에 추가하고 방문으로 표시합니다.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0  # 초기 거리 값을 0으로 설정합니다.
        while q:
            for i in range(len(q)):  # 현재 큐에 있는 모든 위치를 처리합니다.
                r, c = q.popleft()  # 큐에서 위치를 꺼냅니다.
                if grid[r][c] == inf or grid[r][c] == 0:
                    grid[r][c] = dist  # 현재 위치의 거리를 업데이트합니다.
                # 인접한 네 방향으로 방을 추가합니다.
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1  # 다음 거리 값을 증가시킵니다.
