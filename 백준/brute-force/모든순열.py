"""
10974번 문제

N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 
"""

def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True

n = int(input())
arr = [i for i in range(1,n+1)]

print(' '.join(map(str, arr)))
while next_permutation(arr):
    print(' '.join(map(str, arr)))


