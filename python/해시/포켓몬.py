"""
https://school.programmers.co.kr/learn/courses/30/lessons/1845
"""
def solution(nums):
    getNum = len(nums) / 2
    result = list(dict.fromkeys(nums))
    answer = getNum if len(result) > getNum else len(result)
    
    return answer