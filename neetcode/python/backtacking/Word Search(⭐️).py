# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxRow = len(board)
        maxCol = len(board[0]) 
        path = set()

        def dfs( r, c, idx):
            if idx == len(word):
                return True

            if (
                # out of range
                c < 0 
                or r < 0
                or r >= maxRow 
                or c >= maxCol 

                # not correct char
                or board[r][c] != word[idx] or
                (r,c) in path
            ):
                return False
            
            path.add((r,c))

            res = (
                dfs(r+1, c, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1)
            )

            path.remove((r,c))

            return res
        
        for r in range(maxRow):
            for c in range(maxCol):
                if dfs(r,c,0):
                    return True

        return False