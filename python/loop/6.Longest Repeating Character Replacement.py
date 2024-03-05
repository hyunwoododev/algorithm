# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # 문자의 빈도수를 저장할 딕셔너리
        l = 0  # 윈도우의 왼쪽 인덱스
        maxf = 0  # 윈도우 내에서 가장 많이 등장하는 문자의 빈도수
        for r in range(len(s)):  # 윈도우의 오른쪽 인덱스를 이동
            count[s[r]] = 1 + count.get(s[r], 0)  # 현재 문자의 빈도수를 업데이트
            maxf = max(maxf, count[s[r]])  # 가장 빈번한 문자의 빈도수를 업데이트

            # 윈도우의 크기에서 가장 빈번한 문자의 빈도수를 뺀 값이 k보다 크면,
            # 윈도우의 크기를 줄여야 함
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # 왼쪽 인덱스에 해당하는 문자의 빈도수 감소
                l += 1  # 윈도우의 왼쪽 인덱스를 오른쪽으로 이동

        # 최대 윈도우 크기 반환
        return (r - l + 1)


