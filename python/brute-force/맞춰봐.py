"""
-10 ~ 10까지의 정수를 N개 나열한다. 그리고 해당 수열의 모든 구간합이 양수, 음수, 0 중에 어떤 것인지가 주어진다. 
이때, 조건을 만족하는 N개의 수로 이루어진 수열을 하나 출력해야 한다.

skip this !
"""

def backtrack(k, stack):
    temp = k
    candidates = range(-10, 11)
    for i in range(k + 1):
        now = a[temp]
        if now == '+':
            candidates = [c for c in candidates if (sum(stack[i:k]) + c) > 0]
        elif now == '-':
            candidates = [c for c in candidates if (sum(stack[i:k]) + c) < 0]
        else:
            candidates = [c for c in candidates if (sum(stack[i:k]) + c) == 0]
        temp += (n - (i + 1))
    if k == (n - 1) and candidates:
        global ans
        stack[-1] = candidates[0]
        ans = stack
    else:
        for c in candidates:
            if not ans:
                stack[k] = c
                backtrack(k + 1, stack)


n = int(input())
a = input()
ans = []

backtrack(0, [0 for _ in range(n)])
print(*ans)