# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # t 문자열에서 각 문자의 등장 횟수를 카운트하는 딕셔너리
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 필요한 문자의 개수와 현재 창문 안에 있는 문자의 개수를 추적하는 변수 초기화
        have, need = 0, len(countT)
        # 최소 창문의 시작 인덱스와 길이를 저장할 변수 초기화
        res, resLen = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # 현재 문자가 t 문자열에 존재하고 현재 창문 안에 있는 해당 문자의 개수가 t 문자열에서의 해당 문자의 필요 개수와 같다면
            # 필요한 문자의 개수를 증가시킴
            if c in countT and window[c] == countT[c]:
                have += 1

            # 현재 창문 안에 모든 필요한 문자가 포함된 경우
            while have == need:
                # 결과를 업데이트
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # 왼쪽 끝의 문자를 창문에서 제거하고 해당 문자의 개수를 갱신하며 창문을 이동시킴
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        # 결과 반환
        return s[l : r + 1] if resLen != float("infinity") else ""
