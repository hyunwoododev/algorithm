#  1749 문제

# 주어진 자연수 N까지의 모든 자연수를 이어서 쓸 때, 총 몇 자리 숫자가 되는지 구하는 프로그램을 작성하라.

# 입력:
# 첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.

# 출력:
# 첫째 줄에 총 몇 자리 숫자가 되는지 출력한다.

n = int(input())
ans = 0
start = 1
length = 1
while start <= n:
    end = start*10-1
    if end > n:
        end = n
    ans += (end-start+1)*length
    start *= 10
    length += 1
    
print(ans)