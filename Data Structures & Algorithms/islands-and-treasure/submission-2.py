from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq = deque([])
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    dq.append((x,y))
        while dq:
            tx, ty = dq.popleft()
            for drx,dry in [(1,0),(-1,0),(0,1),(0,-1)]:
                newx, newy = tx+drx, ty+dry
                if 0<=newx<len(grid[0]) and 0<=newy<len(grid) and grid[ty][tx] +1 <grid[newy][newx]:
                    dq.append((newx,newy))
                    grid[newy][newx] = grid[ty][tx] +1
