class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        if n < 0:
            for _ in range(abs(n)):
                res = res *(1.0/x)
        elif n>0:
            for _ in range(n):
                res = res * x
        return res