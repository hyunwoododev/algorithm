# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem?isFullScreen=true

# 사용자로부터 막대기의 개수 N을 입력받음
N = int(input())
# 공백으로 구분된 N개의 막대기 길이를 입력받아 정수 리스트로 변환
sticks = list(map(int, input().split()))

# 막대기 길이를 내림차순으로 정렬
sticks.sort()
sticks.reverse()

# 가장 큰 삼각형의 변 길이를 저장할 변수 초기화 (존재하지 않는 경우를 처리하기 위해 None으로 초기화)
maximum = None

# 모든 막대기에 대해 반복
for index, stick in enumerate(sticks):
    # 현재 막대기가 리스트의 끝에서 세 번째 이상의 위치에 있지 않다면, 
    # 삼각형을 만들 수 있는 충분한 막대기가 없으므로 반복 중단
    if index > len(sticks)-3:
        break
    # 삼각형 성립 조건 검사: 두 번째와 세 번째로 긴 막대기의 합이 가장 긴 막대기보다 길어야 함
    if sticks[index+1] + sticks[index+2] > stick:
        # 삼각형 성립 조건을 만족하는 경우, 해당 막대기 길이를 maximum 변수에 튜플로 저장
        maximum = (sticks[index+2], sticks[index+1], sticks[index])
        # 적합한 삼각형을 찾았으므로 반복 중단
        break

# maximum 변수가 None이 아니라면 적합한 삼각형을 찾은 것이므로,
# 해당 막대기 길이를 공백으로 구분하여 출력
if maximum:
    print(" ".join(map(str, maximum)))
# 적합한 삼각형을 찾지 못한 경우 -1 출력
else:
    print(-1)
