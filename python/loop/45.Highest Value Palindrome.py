# https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true
l, k = input().split(' ')
l = int(l)
k = int(k)
n = list(input())
midl = int(len(n)/2)


diff = 0
for i in range(0,midl):
    if (n[i] != n[l-1-i]):
        diff += 1

if (diff > k):
    print(-1)
    exit(0)

more = k - diff

count = 0
for i in range(0,midl):
    if (n[i] == n[l-1-i]):
        if (n[i] != '9' and more >= 2):
            n[i], n[l-1-i] = '9', '9'
            more -= 2
        continue

    maxn = n[i] if (n[i] > n[l-1-i]) else n[l-1-i]
    if (maxn != '9' and more >= 1):
        more -= 1
        maxn = '9'
    n[i], n[l-1-i] = maxn, maxn

if (more > 0):
    n[midl] = '9'
        
print("".join(n))
    