# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있습니다.
#  1+1+1+1, 1+1+2, 1+2+1, 1+3, 2+1+1, 2+2, 3+1
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하세요.

def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return solve(n-1) + solve(n-2) + solve(n-3)

t = int(input())

for _ in range(t):
    n = int(input())
    print(solve(n))

