class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(lp,rp):
            if lp == rp == n:
                res.append("".join(cur))
            if lp < n:
                cur.append("(")
                dfs(lp+1,rp)
                cur.pop()
            if rp < lp:
                cur.append(")")
                dfs(lp,rp+1)
                cur.pop()
        dfs(0,0)
        return res
            