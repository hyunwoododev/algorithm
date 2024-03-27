"""
14226번 문제

영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.
영선이는 이미 화면에 이모티콘 1개를 입력했다. 

이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.
1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
3. 화면에 있는 이모티콘 중 하나를 삭제한다.

모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 
클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다.
화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.
영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 S (2 ≤ S ≤ 1000) 가 주어진다.
첫째 줄에 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

s = int(input().strip())
visited = [[0] * 1001 for _ in range(1001)]  # 카운트 세는 리스트

def bfs():
    q = deque()
    ans = 0
    q.append((1, 0))  # (화면에 존재하는 이모티콘 개수,현재 클립보드에 저장된 이모티콘 개수)
    while q:
        x_screen, x_clip = q.popleft()
        if x_screen == s:
            ans = visited[x_screen][x_clip]
            break

        arr = [
            (x_screen, x_screen),
            (x_screen + x_clip, x_clip),
            (x_screen - 1, x_clip),
        ]

        for screen, clip in arr:
            if 0 <= screen < 1001 and 0 <= clip < 1001 and not visited[screen][clip]:
                # 첫 번째 경우
                q.append((screen, clip))  # 현재 화면에 존재하는 이모티콘 개수 만큼 클립보드에 저장
                visited[screen][clip] = visited[x_screen][x_clip] + 1

    return ans


print(bfs())


