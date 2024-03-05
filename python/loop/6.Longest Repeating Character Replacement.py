# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxf = 0  # 윈도우 내에서 가장 많이 등장하는 문자의 빈도수

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1 

        # 최대 윈도우 크기 반환
        return (r - l + 1)


