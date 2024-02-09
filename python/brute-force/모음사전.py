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

# itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.
# 제공하는 클래스는 매우 다양하지만, 코딩 테스트에서 가장 유용하게 사용할 수 있는 클래스는 permutations, combinations이다.
# permutations(순열)
# ex) 4개의 서로 다른 공 중에서 2개를 골라 나열하는 경우의 수
# 순열은 순서가 중요하므로, A B 와 B A 는 다른 경우로 취급
# nPr = n! / (n-r)!
# combinations(조합)
# ex) 4개의 공중에서 무작위로 2개의 공을 고르는 경우의 수
# 조합은 순서가 중요하지 않으므로, A B 와 B A 는 같은 경우로 취급
# nCr = n! / ((n-r)! * r!)