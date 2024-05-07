# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxRef = 0
        for r in range(len(s)):

            # 가장 많이 등장하는 알파벳의 빈도 카운트
            currentValue = s[r]
            count[currentValue] = count.get(currentValue,0) + 1
            maxRef = max(maxRef, count[currentValue])

            # 현재 윈도우의 길이 내 k갯수만큼 수정해도 연속된 알파벳으로 만들 수 없는 경우 
            if (r-l+1) - maxRef > k:
                # 윈도우 최대 길이를 유지하며 다음 라인을 확인한다.
                count[s[l]] -= 1
                l += 1
        return r - l + 1






