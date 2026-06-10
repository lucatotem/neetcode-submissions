from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque([])
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    dq.append((x,y))
        curMax = 0
        while dq:
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            x,y = dq.popleft()
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<len(grid[0]) and 0<=ny<len(grid) and (grid[ny][nx] == 1 or grid[ny][nx] > grid[y][x]) and grid[ny][nx] != 0:
                    grid[ny][nx] = grid[y][x]+1
                    dq.append((nx,ny))
                    curMax = max(curMax,grid[ny][nx]-2)
                    

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    return -1
        return curMax