"""
14002번 문제

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 
A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.
"""

import sys

N = int(sys.stdin.readline())
Arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

for i in range(N):  # 배열 길이만큼돈다.
    for j in range(i):  # 해당 배열 원소의 직전 원소까지 돈다.
        if Arr[i] > Arr[j]:  # 만약 해당 원소가 전 원소보다 크다면
            dp[i] = max(dp[i], dp[j] + 1)
            # 전 원소에 저장되어 있는 최장수열길이에서 +1 값과 저장되어있는 수열길이값을 비교해서 큰값을 대입

print(max(dp)) #dp 배열 중 가장 큰값

# 여기 부터 어렵네.
subsequence = [] #정답수열 입력할 배열선언
order = max(dp)  # max(dp) 값을 저장
for i in range(N - 1, -1, -1):
    if dp[i] == order:  # 만약 dp[i] 값이 order값과 같다면
        subsequence.append(Arr[i])  # 해당 Arr[i]값을 추가
        order -= 1  # 해당 order 값을 1씩 감소시킨다.

subsequence.reverse()  # 큰수부터 작은수로 뽑았기 때문에
print(*subsequence) #정답수열 출력