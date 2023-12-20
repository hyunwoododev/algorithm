"""
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 
예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다. 
자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, 
f(A)로 표현한다. 
x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.
자연수 N이 주어졌을 때, g(N)을 구해보자.
"""
import sys
input = sys.stdin.readline

# 최대값 설정
MAX=1000000

# DP 1로 초기화
dp = [1]*(MAX+1)
# S: 값 누적 리스트
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j=1
    while i*j <= MAX:
    	# i의 배수에 값 추가
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
	# 누적 값 계산
    s[i] = s[i-1] + dp[i]

n = int(input())
ans=[]
for _ in range(n):
    a=int(input())
    ans.append(s[a])

print('\n'.join(map(str, ans))+'\n')
