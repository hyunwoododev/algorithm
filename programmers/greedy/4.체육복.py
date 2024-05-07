# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    # set으로 변환하여 중복 제거
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    # 체육복 빌려주기
    for r in reserve_set:
        # 앞 번호의 학생에게 빌려줄 수 있는 경우
        if r-1 in lost_set:
            lost_set.remove(r-1)
        # 뒷 번호의 학생에게 빌려줄 수 있는 경우
        elif r+1 in lost_set:
            lost_set.remove(r+1)
    
    # 전체 학생 수에서 잃어버린 학생 수를 뺀 값 반환
    return n - len(lost_set)
