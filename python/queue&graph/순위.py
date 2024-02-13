"""
https://school.programmers.co.kr/learn/courses/30/lessons/49191
"""
from collections import deque

def solution(n, results):
    win = {x: set() for x in range(1, n+1)}
    lose = {x: set() for x in range(1, n+1)}
    
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
    
    for i in range(1, n+1):
        # i에게 진 선수들은 i를 이긴 모든 선수에게 짐
        for loser in lose[i]:
            win[loser].update(win[i])
        # i에게 이긴 선수들은 i에게 진 모든 선수에게 이김
        for winner in win[i]:
            lose[winner].update(lose[i])
            
    answer = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
            
    return answer
