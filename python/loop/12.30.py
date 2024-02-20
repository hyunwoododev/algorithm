# https://www.acmicpc.net/problem/10610

n = sorted(list(input()), reverse=True)
sum = sum(map(int, n))

# 사실은 1의 자리가 0임을 체크해야 10의 배수임을 체크하는 것이 맞다.
# 하지만, 0이 있는지만 체크하는건 어차피 소팅해놨기 때문에 어차피 맨 뒤에 있을 것이다.
# 이 문제의 핵심은 스트링과 정수형을 이해하는것.
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))