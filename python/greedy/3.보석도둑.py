# https://www.acmicpc.net/problem/1202
# 각 가방에 담을 수 있는 최대 가치의 보석을 담되 용량이 작은 가방부터 보석을 담는다.
import sys
import heapq

N, K = map(int, sys.stdin.readline().split()) # 보석의 개수, 가방의 개수

# jew[] 에는 보석의 무게와 가치를 저장한다. 
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))

# bags[] 에는 가방의 용량을 저장한다.
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

# 가방의 용량을 오름차순으로 정렬한다.    
bags.sort()

answer = 0
tmp_jew = []
for bag in bags:
    # 각 가방에 대해서 반복한다. 가방은 용량이 작은 것부터 정렬되어 있다.
    
    while jew and bag >= jew[0][0]:
        # 현재 가방의 용량보다 작거나 같은 보석이 있다면, 그 보석을 가능한 후보군에 추가한다.
        # jew 힙에서 가장 작은 무게의 보석을 확인하고, 가방에 담을 수 있으면 후보군(tmp_jew)에 추가한다.
        # tmp_jew는 가치가 큰 보석부터 꺼낼 수 있도록 가치를 음수로 저장하여 최대 힙처럼 사용한다.
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        # 후보군(tmp_jew)에 보석이 있으면, 가장 가치가 높은 보석을 꺼내어 총 가치에 추가한다.
        # 가치가 음수로 저장되어 있으므로, 실제 가치를 얻기 위해 음수로 다시 변환한다.
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        # 모든 보석이 고려되었으면 반복을 중단한다.
        break
print(answer)