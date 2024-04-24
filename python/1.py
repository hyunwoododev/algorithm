def calculate_custom_keypad_times(mapping, number):
    # 매핑된 키패드를 좌표로 변환
    keypad = {str(mapping[row][col]): (row, col) for row in range(3) for col in range(3)}

    # 입력된 숫자를 문자열로 변환
    digits = str(number)

    # 첫 번째 숫자의 위치에서 시작
    current_position = keypad[digits[0]]
    times = [0]  # 시작 위치는 0초로 계산

    # 각 숫자에 대하여 이동 시간 계산
    for i in range(1, len(digits)):
        digit = digits[i]
        next_position = keypad[digit]
        # 최소 이동 거리는 맨해튼 거리
        time = abs(next_position[0] - current_position[0]) + abs(next_position[1] - current_position[1])
        times.append(time)
        current_position = next_position

    return times

# 매핑된 키패드
mapping = [
    [9, 2, 3],
    [8, 5, 7],
    [6, 1, 4]
]

# 예제 번호
number = 923857614
times = calculate_custom_keypad_times(mapping, number)
print(times)
