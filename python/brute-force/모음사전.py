"""
https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3
"""

from itertools import product
def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']
    for i in range(1,6):
        for per in product(li,repeat = i):
            answer.append(''.join(per))

    answer.sort()
    return answer.index(word)+1 # 🤪틀렸던 부분, 0부터 시작하므로 +1

