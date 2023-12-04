"""
짝수를 두 소수의 합으로 나타내는 문제로, 4보다 큰 모든 짝수는 두 소수의 합으로 표현할 수 있다는 골드바흐의 추측을 따릅니다.
이 문제를 해결하기 위해서는 먼저 주어진 범위 내의 모든 소수를 찾은 다음, 각 짝수를 두 소수의 합으로 표현하는 방법을 찾아야 합니다.
"""

import sys
number = [True] * 1000001
# 소수 리스트 생성
for i in range(2, int(len(number) ** 0.5) + 1):
    if number[i]:
        for j in range(2 * i, 1000001, i):
            number[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    # 2부터 시작하여 n의 절반까지 확인. 일부러 2씩 건너뛰어서 짝수는 제외
    for i in range(3, n // 2 + 1, 2):
        if number[i] and number[n - i]:
            print(f"{n} = {i} + {n - i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')


