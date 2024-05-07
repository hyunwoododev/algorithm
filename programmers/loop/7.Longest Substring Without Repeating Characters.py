# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        charSet = set()
        maxRef = 1 
        l = 0
        for r in range(len(s)):
            newChar = s[r]

            # 새로운 문자와 중복이 없어질때까지 l 제거
            while newChar in charSet:
                leftValue = s[l]
                charSet.remove(leftValue)
                l += 1

            charSet.add(s[r])  
            maxRef = max(maxRef, r-l+1)

        return maxRef
