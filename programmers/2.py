def count_pairs_with_difference_of_two(nums):
    # 배열을 정렬
    nums.sort()
    
    left = 0
    right = 0
    pair_count = 0
    n = len(nums)
    
    # 두 포인터 기법을 사용하여 배열 스캔
    while right < n:
        if nums[right] - nums[left] < 2:
            right += 1  # 차이가 2 미만이면 right를 증가
        elif nums[right] - nums[left] > 2:
            left += 1  # 차이가 2 초과이면 left를 증가
        else:
            pair_count += 1  # 차이가 정확히 2면 카운트 증가
            left += 1  # 쌍을 찾았으므로 left를 이동하여 다음 쌍을 찾음

    return pair_count

# 입력 배열
nums = [1, 3, 5, 7, 9]
# 함수 실행 및 결과 출력
result = count_pairs_with_difference_of_two(nums)
print(result)
