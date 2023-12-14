"""
14501번

상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.
백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
N = 7인 경우에 다음과 같은 상담 일정표를 보자.
... (이하 생략)
"""

def dfs(day, tmp):
    global ans
    if day == N:
        if ans < tmp:
            ans = tmp
        return
    
    # 상담을 하지 않는 경우
    dfs(day+1, tmp)
    # 상담을 하는 경우
    if day + a[day][0] <= N: 
        dfs(day+a[day][0], tmp + a[day][1])


N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = 0
dfs(0, 0)
print(ans)
