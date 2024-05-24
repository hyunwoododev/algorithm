# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r, c, v, prevHeight):
            if(
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or (r,c) in v
                or heights[r][c] < prevHeight
            ):
                return

            v.add((r,c))
            for dr,dc in direction:
                row = r + dr
                col = c + dc
                dfs(row,col,v,heights[r][c])
        
        for i in range(COLS):
            dfs(0, i, pac, heights[0][i])
            dfs(ROWS-1, i, atl, heights[ROWS-1][i])

        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS-1, atl, heights[i][COLS-1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c] )
        return res

            
            