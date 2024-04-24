def select_employees(scores, team_size, k):
    selected_scores_sum = 0  # 선택된 직원들의 점수 합을 저장할 변수

    while team_size > 0 and scores:
        # 선택 범위 설정: 점수 리스트의 길이가 k보다 작으면 전체 리스트에서 선택
        if len(scores) <= k:
            selected_index = scores.index(max(scores))
        else:
            # 첫 k개 원소와 마지막 k개 원소 중 최대값을 찾기
            first_k = scores[:k]
            last_k = scores[-k:]
            max_first_k = max(first_k)
            max_last_k = max(last_k)

            # 첫 k개와 마지막 k개 원소 중 최대값을 비교하여 선택
            if max_first_k > max_last_k:
                selected_index = first_k.index(max_first_k)
            elif max_last_k > max_first_k:
                selected_index = len(scores) - k + last_k.index(max_last_k)
            else:  # 두 값이 같을 경우 더 낮은 인덱스 선택
                selected_index = first_k.index(max_first_k) if first_k.index(max_first_k) <= len(scores) - k + last_k.index(max_last_k) else len(scores) - k + last_k.index(max_last_k)

        # 선택된 점수 합계 업데이트
        selected_scores_sum += scores[selected_index]
        # 선택된 직원 점수 삭제
        del scores[selected_index]
        
        # 팀 크기 감소
        team_size -= 1

    return selected_scores_sum

# 예제 데이터
scores = [10, 20, 10, 15, 5, 30, 20]
team_size = 2
k = 3

# 함수 실행 및 결과 출력
result = select_employees(scores, team_size, k)
print("Sum of selected employees' scores:", result)
