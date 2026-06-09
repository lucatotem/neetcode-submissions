class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(x,y,i):
            if board[y][x] == word[i]:
                if i==len(word)-1:
                    return True
                temp = board[y][x]
                board[y][x] = "."
                if x>0 and dfs(x-1,y,i+1):
                    return True
                elif y>0 and dfs(x,y-1,i+1):
                    return True
                elif x<len(board[0])-1 and dfs(x+1,y,i+1):
                    return True
                elif y<len(board)-1 and dfs(x,y+1,i+1):
                    return True
                board[y][x] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(j,i,0):
                    return True
        return False