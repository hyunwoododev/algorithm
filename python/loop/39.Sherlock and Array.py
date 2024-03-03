# # https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true

# import sys

# # 테스트 케이스의 수를 입력받음
# T = int(sys.stdin.readline())

# # 각 테스트 케이스에 대해
# for t in range(T):
#     # 배열의 크기 N을 입력받음
#     N = int(sys.stdin.readline())
#     # 배열의 원소들을 입력받아 정수 리스트로 변환
#     elements = [int(nbr) for nbr in sys.stdin.readline().split()]
    
#     # 왼쪽 부분의 합을 저장할 리스트와 누적 합 변수 초기화
#     leftarr = []
#     ack = 0
#     leftarr.append(ack)  # 초기 누적 합 0 추가
#     # 각 원소에 대해 왼쪽 부분의 누적 합 계산
#     for element in elements:
#        ack += element
#        leftarr.append(ack)
    
#     # 오른쪽 부분의 합을 저장할 리스트와 누적 합 변수 초기화
#     rightarr = []
#     rightack = 0
#     rightarr.append(rightack)  # 초기 누적 합 0 추가
#     pos = len(leftarr) - 1  # 왼쪽 부분의 누적 합 리스트의 마지막 인덱스
#     # 배열의 원소들을 역순으로 순회하면서 오른쪽 부분의 누적 합 계산
#     for elements in reversed(elements):
#         rightack += elements
#         # 현재 위치에서 왼쪽 부분의 누적 합과 오른쪽 부분의 누적 합이 같으면 "YES" 출력
#         if leftarr[pos] == rightack:
#             print("YES")
#             break
#         pos -= 1  # 다음 위치로 이동
#         # 모든 원소를 확인했을 때 균형점을 찾지 못하면 "NO" 출력
#         if pos == 0:
#             print("NO")
#             break


for t in range(int(input())):
    n = int(input())
    arr = [int(b) for b in input().split()]
    answer = "NO"
    for i in range(n):
        if i == 0:
            if 0 == sum(arr[1:n]):
                answer = "YES"
                break
        elif i == n-1:
            if arr[-1] == sum(arr[:-2]):
                answer = "YES"
                break
        else:
            break
                