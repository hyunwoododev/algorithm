# https://leetcode.com/problems/climbing-stairs/description/

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0] * n
#         dp[0] = 1
#         dp[1] = 1
#         for i in range(2,n):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]
        

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
