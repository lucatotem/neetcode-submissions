from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(x,y,l,s):
            dq = deque([])
            dq.append((x,y))
            board[y][x] = s
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while dq:
                x,y= dq.popleft()
                for dx, dy in dirs:
                    nx, ny = dx+x,dy+y
                    print(nx,ny)
                    if 0<= nx < len(board[0]) and 0<=ny<len(board) and board[ny][nx] == l:
                        board[ny][nx] = s
                        dq.append((nx,ny))
        for y in range(len(board)):
            if board[y][0] == "O":
                bfs(0,y,"O",".")
            if board[y][len(board[0])-1] == "O":
                bfs(len(board[0])-1,y,"O",".")
        for x in range(len(board[0])):
            if board[0][x] == "O":
                bfs(x,0,"O",".")
            if board[len(board)-1][x] == "O":
                bfs(x,len(board)-1,"O",".")
        print(board)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "O":
                    bfs(x,y,"O","X")
        for y in range(len(board)):
            if board[y][0] == ".":
                bfs(0,y,".","O")
            if board[y][len(board[0])-1] == ".":
                bfs(len(board[0])-1,y,".","O")
        for x in range(len(board[0])):
            if board[0][x] == ".":
                bfs(x,0,".","O")
            if board[len(board)-1][x] == ".":
                bfs(x,len(board)-1,".","O")


