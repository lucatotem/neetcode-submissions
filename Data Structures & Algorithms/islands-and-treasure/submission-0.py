from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(x,y):
            dq = deque([(x,y,0)])
            while dq:
                tx, ty, dist = dq.popleft()
                if grid[ty][tx] != -1 and grid[ty][tx] >= dist:
                    grid[ty][tx] = dist
                    for drx,dry in [(1,0),(-1,0),(0,1),(0,-1)]:
                        newx, newy = tx+drx, ty+dry
                        if 0<=newx<len(grid[0]) and 0<=newy<len(grid):
                            dq.append((newx,newy,dist+1))


        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    bfs(x,y)
