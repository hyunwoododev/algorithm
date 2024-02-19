# https://www.acmicpc.net/problem/10610

# 사용자로부터 문자열 형태로 숫자를 입력 받음
n = input()
# 입력 받은 숫자들을 내림차순으로 정렬
n = sorted(n, reverse=True)
# 모든 숫자의 합을 저장할 변수 초기화
sum = 0

# 가장 큰 수를 만들기 위해선 0이 포함되어 있어야 하며, 그렇지 않은 경우 -1을 출력
if '0' not in n:	
    print(-1)
else:
    # 숫자들의 합을 구함
    for i in n:
        sum += int(i)
    # 숫자들의 합이 3의 배수인지 확인
    if sum % 3 != 0 :	
        print(-1)
    else :
        # 조건을 만족하는 경우, 내림차순으로 정렬된 숫자들을 합쳐 출력
        print(''.join(n))