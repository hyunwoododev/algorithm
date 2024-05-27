# https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem?isFullScreen=true

def hackerlandRadioTransmitters(x, k):
    x.sort()  # 집 위치를 정렬합니다.
    i = 0
    n = len(x)
    num_transmitters = 0

    while i < n:
        num_transmitters += 1  # 송신기 설치
        loc = x[i] + k  # 현재 위치에서 k만큼 오른쪽으로 이동

        # 송신기를 설치할 최적의 위치를 찾습니다.
        while i < n and x[i] <= loc:
            i += 1

        # 송신기의 커버리지가 끝나는 지점을 찾습니다.
        loc = x[i - 1] + k

        while i < n and x[i] <= loc:
            i += 1

    return num_transmitters

# 예제 입력
n, k = map(int, input().split())
x = list(map(int, input().split()))

# 결과 출력
print(hackerlandRadioTransmitters(x, k))
