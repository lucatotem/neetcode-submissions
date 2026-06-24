class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl, pac = set(), set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r, c, st):
            if (r,c) in st:
                return
            else:
                st.add((r,c))
                for dr,dc in directions:
                    nr,nc = dr + r, dc + c
                    if 0<= nr < len(heights) and 0<= nc < len(heights[0]) and heights[r][c] <= heights[nr][nc]:
                        dfs(nr,nc,st)
        for i in range(len(heights)):
            dfs(i,0,pac)
            dfs(i,len(heights[0])-1,atl)
        for i in range(len(heights[0])):
            dfs(0,i,pac)
            dfs(len(heights)-1,i,atl)
        res= []
        for c in range(len(heights[0])):
            for r in range(len(heights)):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res

