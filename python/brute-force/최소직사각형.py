"""
https://school.programmers.co.kr/learn/courses/30/lessons/86491
"""
def solution(sizes):
    answer = max([max(x) for x in sizes]) * max([min(x) for x in sizes])
    return answer