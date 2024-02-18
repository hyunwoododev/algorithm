# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people=list(people)
    people.sort()
    
    x=0
    y=len(people)-1
    
    while x < y:   
        if people[x] + people[y] <= limit:  # 작은 수와 큰 수를 더한 값이 limit보다 작으면 카운트를 증가하고 x,y를 제외한다.
            x+=1
        y-=1
        answer +=1

        if x==y:                            # 인덱스가 같은 경우 보트하나 추가하고 종료
            answer +=1

    return answer