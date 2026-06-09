class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def bfs(x,y):
            if grid[y][x]== "1":
                grid[y][x] = "0"
                if x>0:
                    bfs(x-1,y)
                if y>0:
                    bfs(x,y-1)
                if x<len(grid[0])-1:
                    bfs(x+1,y)
                if y<len(grid)-1:
                    bfs(x,y+1)
            


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(j,i)
                    count+=1
        return count