"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) 
M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
"""
"""
에라토스테네스의 체
- 배수를 지우는 방식으로 소수를 찾는 방법
- 즉 소수를 찾는거니깐, 배수들은 소수가 아니니깐 배수들을 전부 지워버리면 소수만 남는다.
"""

def sieve_of_eratosthenes(m, n):
    prime = [True for _ in range(n+1)]
    prime[0], prime[1] = False, False

    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n+1, i): # 파이썬 range의 3번째 인자는 증가폭을 의미한다. 즉, i의 배수를 지우는 것이다.
                prime[j] = False

    for i in range(m, n+1):
        if prime[i]:
            print(i)

# 메인 로직
M, N = map(int, input().split())
sieve_of_eratosthenes(M, N)
