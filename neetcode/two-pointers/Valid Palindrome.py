# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for a in s:
            if a.isalpha() or a.isdigit():
                new += a.lower()
        return (new == new[::-1])

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            
            if not s[l].isalnum():
                l += 1
                
            elif not s[r].isalnum():
                r -= 1

            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                
            else:
                return False
     
        return True