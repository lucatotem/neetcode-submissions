class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, summ):
            if summ == target:
                res.append(cur.copy())
                return
            elif i == len(candidates) or summ > target:
                return
            else:
                cur.append(candidates[i])
                dfs(i+1,cur,summ+candidates[i])
                cur.pop()
                while i != len(candidates)-1 and candidates[i] == candidates[i+1]:
                    i+= 1
                dfs(i+1,cur,summ)
        dfs(0,[],0)
        return res