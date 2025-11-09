class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. 구간 리스트 정렬 (시작 값 기준)
        intervals.sort(key=lambda x: x[0])

        # 2. 결과 리스트 초기화
        output = [intervals[0]]

        # 3. 구간 순회
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]  # 결과 리스트의 마지막 구간의 끝 값

            if start <= lastEnd:
                # 겹치는 경우, 병합하여 마지막 구간 업데이트
                output[-1][1] = max(lastEnd, end)
            else:
                # 겹치지 않는 경우, 새로운 구간 추가
                output.append([start, end])

        return output
