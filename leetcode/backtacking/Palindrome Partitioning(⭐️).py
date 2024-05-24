# https://leetcode.com/problems/palindrome-partitioning/description/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, stack = [], []

        def dfs(i):
            if i >= len(s):
                res.append(stack[:])
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    stack.append(s[i : j + 1])
                    dfs(j + 1)
                    stack.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
