# 문제 : 
# 현재 채널: 100
# 목표 채널: N (0 ≤ N ≤ 500,000)
# 고장난 버튼의 개수: M
# 고장난 버튼의 번호: 주어짐 (0 ~ 9)
# 주의사항:

# 리모컨에는 +와 - 버튼도 있다. + 버튼은 채널을 1 증가시키고, - 버튼은 1 감소시킨다.
# 숫자 버튼, + 버튼, - 버튼을 적절히 이용해서 목표 채널로 이동하는 최소 클릭 횟수를 구한다.
# 이 문제를 풀기 위해서는 2가지 주요 전략을 사용합니다:

# +, - 버튼만 사용하여 목표 채널로 이동하는 경우
# 숫자 버튼을 최대한 활용하여 목표 채널에 근접한 위치로 이동한 뒤 +, - 버튼으로 조절하는 경우

# 풀이 :
def possible(channel):
    for ch in str(channel):
        if ch in broken_buttons:
            return False
    return True

N = int(input())
M = int(input())
broken_buttons = set(input().split()) if M != 0 else set()

min_press = abs(N - 100)  # +, - 버튼만 사용하여 이동하는 경우

for channel in range(1000001):  # 모든 채널 범위를 확인
    if possible(channel):
        min_press = min(min_press, len(str(channel)) + abs(channel - N))

print(min_press)
