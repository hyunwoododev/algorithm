# https://www.acmicpc.net/problem/1931

N= int(input())
time = []
for _ in range(N):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x:(x[1], x[0]))
ans  = 0
currentEnd = 0
for s, e in time:
    if s >= currentEnd:
        ans += 1
        currentEnd = e
print(ans)

