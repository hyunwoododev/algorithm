# https://www.acmicpc.net/problem/11000
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x:x[0])
room = []
for s,e in arr:
    # 방이 하나도 없으면 하나 만들어
    if not room:
        heapq.heappush(room,e)
    else:
        # 가장 빨리끝나는 방을 이어서 쓸 수 있으면, 그 방의 끝나는 시간을 업데이트 해줘
        if room[0] <= s:
            heapq.heappop(room)
            heapq.heappush(room,e)
        else:
            # 가장 빨리끝나도 시작시간이 더 빠르면, 그냥 하나 더 개설해.
            heapq.heappush(room,e)

print(len(room))
        
