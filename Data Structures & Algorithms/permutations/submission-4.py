class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        c = set()
        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for n in nums:
                if n not in c:
                    cur.append(n)
                    c.add(n)
                    dfs()
                    c.remove(n)
                    cur.pop()

        dfs()
        return res