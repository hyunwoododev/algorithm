# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 현재 부분 문자열에서 고유한 문자를 추적하기 위해 빈 집합을 초기화합니다.
        charSet = set()
        # 슬라이딩 윈도우의 왼쪽 포인터를 0으로 초기화합니다.
        l = 0
        # 반복되는 문자가 없는 부분 문자열의 최대 길이를 저장하기 위해 결과 변수를 초기화합니다.
        res = 0

        # 오른쪽 포인터 'r'로 문자열을 순회합니다.
        for r in range(len(s)):
            # 오른쪽 포인터 'r'의 문자가 이미 집합에 있으면 (즉, 반복되는 문자임),
            # 반복되는 문자가 집합에서 제거될 때까지 윈도우의 왼쪽에서 문자를 계속 제거하고 왼쪽 포인터 'l'을 오른쪽으로 이동시킵니다.
            while s[r] in charSet:
                # 왼쪽 포인터 'l'의 위치에 있는 문자를 집합에서 제거하고 왼쪽 포인터를 오른쪽으로 이동합니다.
                charSet.remove(s[l])
                l += 1
                
            # 현재 오른쪽 포인터 'r'의 문자를 집합에 추가합니다.
            charSet.add(s[r])
            # 결과 변수를 업데이트하여 현재 부분 문자열의 길이와 이전에 계산된 최대 길이 중 더 큰 값을 저장합니다.
            res = max(res, r - l + 1)

        # 계산된 최대 길이를 반환합니다.
        return res

