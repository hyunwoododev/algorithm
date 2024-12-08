'''
11722번 문제

수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 
A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.
'''

import sys

N = int(sys.stdin.readline())
Arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * N
for i in range(N):
    for j in range(i):
        if Arr[i] < Arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp)) 
