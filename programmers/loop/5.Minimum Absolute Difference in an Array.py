# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true

# 두수의 abs란 무엇이가. -> 두 수의 차이를 보고싶은거다.
n = int(input())
arr = list(map(int, input().split()))

if n == 2:
    print(abs(arr[0]-arr[1]))
    exit()

arr.sort()
minRef = 1e9
for i in range(1, n):
    minRef = min(arr[i]-arr[i-1], minRef)
print(minRef)

