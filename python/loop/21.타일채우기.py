"""
https://www.acmicpc.net/problem/2133
"""

import sys

n = int(sys.stdin.readline())
dp = [0] * 31
dp[2] = 3

# 반복문을 통해 점화식을 수행
for i in range(4, n + 1):
    # 짝수만을 타일로 채울 수 있다.
    if i % 2 == 0:
        dp[i] += dp[i - 2] * dp[2]
        dp[i] += 2 # 특수한 모양 2개 추가

        for j in range(i - 4, -1, -2):
            dp[i] += dp[j] * 2 # dp[j]에 특수한 모양 2개의 조합

print(dp[n])






