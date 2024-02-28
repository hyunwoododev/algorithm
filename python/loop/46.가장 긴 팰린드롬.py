# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def palindrome(s):
    if len(s) < 2 or s == s[::-1]:
        return True

def solution(s):

    if len(s) < 2 or s == s[::-1]:
        return len(s)

    for cur in range(len(s), 0, -1): # 즉, cur는 부분 문자열의 길이
        for start in range(len(s)): 
            currS = s[start: start + cur]

            if palindrome(currS):
                return len(currS)
            
            if start + cur > len(s):
                break

