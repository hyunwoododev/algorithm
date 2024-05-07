# https://www.acmicpc.net/problem/11000
import sys
import heapq
input = sys.stdin.readline

N = int(input())  # 수업의 개수 N을 입력 받음
time = []  # 수업 시간을 저장할 리스트

for _ in range(N):
    time.append(list(map(int, input().split(' '))))  # 각 수업의 시작 시간과 종료 시간을 리스트에 추가
time.sort(key=lambda x: x[0])  # 수업을 시작 시간 기준으로 정렬

heap = []  # 현재 진행 중인 수업들의 종료 시간을 관리할 힙(우선순위 큐)
for s, t in time:
    if heap and heap[0] <= s:  # 힙이 비어있지 않고, 가장 빨리 끝나는 수업이 현재 수업의 시작 시간보다 이르거나 같은 경우 = 하나의 강의실에서 연이어 두 수업을 진행할 수 있음을 의미합니다.
        heapq.heappop(heap)  # 해당 수업이 끝났으므로 힙에서 제거
    heapq.heappush(heap, t)  # 현재 수업의 종료 시간을 힙에 추가

print(len(heap))  # 필요한 강의실의 개수는 힙의 크기와 같음
