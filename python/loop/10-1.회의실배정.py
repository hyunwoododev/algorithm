# https://www.acmicpc.net/problem/1931
# solved!
N = int(input())
arr = []
for _ in range(N):
    start,end = map(int,input().split())
    arr.append((start,end))
arr.sort(key=lambda x:[x[1],x[0]])
now = 0
cnt = 0
for start, end in arr:
    if now <= start:
        cnt += 1 
        now = end
print(cnt)


