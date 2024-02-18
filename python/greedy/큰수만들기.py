# https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = []
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return ''.join(answer[:len(answer) - k])