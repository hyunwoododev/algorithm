# https://www.acmicpc.net/problem/11399
# solved !

N = int(input())
M = list(map(int,input().split()))
M.sort()
answer = 0
for i in range(len(M)):
    answer += sum(M[0:(i+1)])
print(answer)