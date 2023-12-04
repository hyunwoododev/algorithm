"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
"""

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n: # 제곱근까지만 검사하면된다. 왜냐면 약수는 대칭적이기 때문에 
        if n % i == 0:
            return False
        i += 1
    return True

def count_primes(numbers):
    # python에서 true는 1, false는 0이다.
    # 결국 소수의 개수를 세는 것이므로, 소수인지 아닌지를 판별하는 함수를 만들어서
    # 소수이면 1, 소수가 아니면 0을 반환하고, 그것들을 모두 더하면 소수의 개수가 된다.(파이썬 제너레이터)
    return sum(is_prime(num) for num in numbers)

# 메인 로직
n = int(input())  # 숫자의 개수(사실상 필요없음)
numbers = list(map(int, input().split()))  # 공백으로 구분된 숫자들
print(count_primes(numbers))
