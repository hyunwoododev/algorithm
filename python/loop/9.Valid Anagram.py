# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = [0] * 26
        tCount = [0] * 26
        answer = True

        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            tCount[ord(t[i]) - ord('a')] += 1
            sCount[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if tCount[index] != sCount[index]:
                return False

        return answer


        