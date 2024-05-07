"""
https://school.programmers.co.kr/learn/courses/30/lessons/43236
"""

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    low = 1
    high = distance
    answer = 0

    while low <= high:
        mid = (low + high) // 2  # 최솟값

        cur_rock = 0  # 왼쪽 바위
        count = 0  # 제거된 수
        for i in range(len(rocks)):
            pre_rock = rocks[i]  # 오른쪽 바위

            if pre_rock - cur_rock < mid:  # mid보다 작을 경우 제거한다.
                count += 1
            else:
                cur_rock = pre_rock
            if n < count:
                break

        if count <= n:  # mid가 클수록 제거해야 하는 돌이 늘어난다.
            answer = mid
            low = mid + 1

        else:
            high = mid - 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))