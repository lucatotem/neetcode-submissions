from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxC = 0
        def bfs(i,j):
            count = 0
            bfsQ = deque([(i,j)])
            while bfsQ:
                r,c = bfsQ.popleft()
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == 1:
                    count += 1
                    grid[r][c] = 0
                    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                        bfsQ.append((r+dr,c+dc))
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxC = max(bfs(i,j),maxC)
        return maxC