"""
9095번 문제
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
"""

import sys
read = sys.stdin.readline

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 4

for i in range(4, 11):
    cache[i] = sum(cache[i-3:i]) #이게 킥이네

T = int(read())
for _ in range(T):
    print(cache[int(read())])
    


