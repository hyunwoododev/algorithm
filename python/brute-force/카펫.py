"""
https://school.programmers.co.kr/learn/courses/30/lessons/42842
"""
def solution(brown, yellow):
    arr = []
    for i in range(1,int(yellow**0.5)+1):
        if yellow % i == 0:
            arr.append((int(yellow/i), i))
            
    for a,b in arr:
        print(a,b)
        if brown == (a+2)*(b+2) - yellow:
            return [a+2,b+2]