# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/

from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        dic = Counter(s)
        t = []
        ans = []
        for char in s:
            t.append(char)
            dic[char] -= 1
            if dic[char] == 0:
                del dic[char] 
            
            while t and (not dic or min(dic) >= t[-1]):
                ans.append(t.pop())
                
        ans += reversed(t)
        return ''.join(ans)
