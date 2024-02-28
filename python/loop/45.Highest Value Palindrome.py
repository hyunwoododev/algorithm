# https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true

n, k = map(int, input().split())
s = list(input())
f = 0
for i in range(n // 2): 
    f += s[i] != s[n - 1 - i]

if f > k: 
    print(-1)
else:
    for i in range(n // 2):

        if s[i] != s[n - 1 - i]:
            f -= 1
        
        if s[i] == s[n - 1 - i] == '9': 
            continue

        if k == f + 1 and s[i] == s[n - 1 - i] :
            continue
        
        if k - f > 1:
            k -= (s[i] != '9') + (s[n - 1 - i] != '9')
            s[i] = s[n - 1 - i] = '9'
        else:
            s[i] = s[n - 1 - i] = max(s[i], s[n - 1 - i])
            k -= 1

    if n % 2 == 1 and k > 0:
        s[n // 2] = '9'

    print(''.join(s))
