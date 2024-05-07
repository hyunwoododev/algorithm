# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# solved!
"""
people	           limit	return
[70, 50, 80, 50]	100	       3
[70, 80, 50]	    100	       3
"""
def solution(people, limit):
    answer = 0
    people.sort()
    x=0
    y=len(people)-1 
    while x < y:  
        """
        둘이나갈수 있으면 둘다 나간다는 의미로 둘다 포인터 이동.
        둘다 나갈수없으면 제일 뚱땡이 하나만 나감.
        """
        if people[x] + people[y] <= limit:  
            x+=1
        y-=1
        answer +=1
        # 인덱스가 같은 경우 보트하나 추가하고 종료
        if x==y:               
            answer +=1
    return answer