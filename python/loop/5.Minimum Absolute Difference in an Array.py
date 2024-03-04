# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true

n = int(input().strip())  # 원소의 개수 입력
a = list(map(int, input().strip().split(' ')))  # 원소 입력
a.sort()  # 배열을 오름차순으로 정렬
min_diff = a[n-1] - a[0]  # 최대값으로 설정

# 배열을 순회하면서 인접한 원소들 간의 차이를 계산
for i in range(1, n):
    min_diff = min(a[i] - a[i-1], min_diff)  # 최소 차이 업데이트
    
print(min_diff)  # 최소 차이 출력

# 두수의 abs란 무엇이가. -> 두 수의 차이를 보고싶은거다.