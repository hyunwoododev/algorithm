import sys
n = 9
a = [int(input()) for _ in range(n)]
a.sort()
for i in range(0, n):
    for j in range(i+1, n):
        total = 0
        for k in range(0, n):
            if i == k or j == k:
                continue
            total += a[k]
        if total == 100:
            for k in range(0, n):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit(0)