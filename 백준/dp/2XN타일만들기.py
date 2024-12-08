"""
11726번 문제

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
"""
import sys
input = sys.stdin.readline

n = int(input())
dp =[0] *1001
dp[1] = 1
dp[2] = 2

for i in range(3,n+1): 
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
    
print(dp[n])