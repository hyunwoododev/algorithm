# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        def dfs(openCnt, closeCnt, curr):
            if closeCnt == openCnt == n:
                stack.append(curr)
                return
            
            if openCnt > closeCnt:
                dfs(openCnt, closeCnt+1, curr+")")
            
            if openCnt < n:
                dfs(openCnt+1, closeCnt, curr+"(")
        
        dfs(0,0,"")
        return stack