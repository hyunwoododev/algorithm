# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true

n = int(input().strip()) 
a = list(map(int, input().strip().split(' ')))

# 두수의 abs란 무엇이가. -> 두 수의 차이를 보고싶은거다.
a.sort()

min_diff = a[n-1] - a[0]

for i in range(1, n):
    min_diff = min(a[i] - a[i-1], min_diff)
    
print(min_diff)

