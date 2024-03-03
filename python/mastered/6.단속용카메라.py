# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# solved!
def solution(routes):
    routes.sort(key=lambda x:[x[1],x[0]])
    camera = -30001
    cnt = 0
    for s,e in routes:
        if s <= camera <= e:
            continue
        else:
            cnt += 1
            camera = e   
    return cnt