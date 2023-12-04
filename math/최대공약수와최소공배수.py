"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
"""
"""
그냥외워버리자.

2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a > b),
a와 b의 최대공약수는 b와 r의 최대공약수와 같다.

최소공배수는 a, b의 곱을 a, b의 최대 공약수로 나누면 나오게 된다.
"""

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))