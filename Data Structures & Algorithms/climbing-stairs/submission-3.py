class Solution:
    def climbStairs(self, n: int) -> int:
        m = {}
        def cl(s):
            if s in m:
                return m[s]
            if s < 0:
                return 0
            elif s == 0:
                return 1
            else:
                m[s] = cl(s-1) + cl(s-2)
                return m[s]
        return cl(n) 
