"""
10819번 문제

N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.
"""
"""
(3 ≤ N ≤ 8) 이조건 보면 브루트포스로 푸는것도 나쁘지않다.
"""

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def calc(a):
    ans = 0
    for i in range(1, len(a)):
        ans += abs(a[i] - a[i-1])
    return ans

n = int(input())
# list(map(int, input().split())).sort() 이렇게 하면 안됨. sort()는 정렬만 시키고 아무것도 리턴하지 않음.
a = list(map(int, input().split())) 
a.sort()
ans = 0

while True:
    temp = calc(a)
    ans = max(ans, temp)
    if not next_permutation(a):
        break

print(ans)
